"""
Contains some utils and decorator for caching
"""
from functools import wraps
import logging

from django.db.models import Model
from django.core import serializers
from apps.core import redis_service as rs

_logger = logging.getLogger(__name__)


def _dump_model(obj: Model) -> str:
    return serializers.serialize("json", [obj])


def _load_model(obj_str: str) -> Model:
    for obj in serializers.deserialize("json", obj_str):
        return obj.object


def cached_model(timeout):
    """Cached the returned value of a function

    timeout (in seconds) is the expired time, set 0 for no-expired
    IMPORTANT: Only use this decorator for the functions that
    returns an Django's model.
    example:
        @cached_model(900)
        def get_user(user_id: int) -> models.User:
            return models.User.objects.filter(id=user_id).first()
    """

    def _decorator(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            # Make cached key from func signature, eg:
            # foo(3, "hello", abc="xyz") => fx:foo:3:hello:abc-xyz
            key_parts = ["fx:func", func.__name__]
            if args:
                key_parts += list(str(v) for v in args)
            if kwargs:
                kwargs_str = ":".join(f"{k}={v}" for k, v in kwargs.items())
                key_parts.append(kwargs_str)

            cached_key = ":".join(key_parts)
            cached_value = rs.get_key_raw(cached_key)
            if cached_value:
                cached_value = cached_value.decode()
                return _load_model(cached_value)

            result = func(*args, **kwargs)
            # Don't cached None obj
            if not result:
                return result

            # Cached result
            result_str = _dump_model(result)
            rs.set_key(cached_key, result_str, timeout)
            _logger.info(
                f"Stored redis, key: {cached_key}, value: {result_str}, timeout: {timeout}"
            )
            return result

        return wrapper_func

    return _decorator
