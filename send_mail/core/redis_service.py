from typing import Union
import random
from redis.client import Redis
from redis.connection import BlockingConnectionPool
from redis.sentinel import Sentinel
from django.conf import settings

from apps.core import consts


class RedisManager:
    _pools = {}
    _sentinel = None
    _slave_rr_counter = None

    @classmethod
    def get_sentinel(cls) -> Union[Sentinel, Redis]:
        if cls._sentinel:
            return cls._sentinel

        redis_sentinel = settings.REDIS_SENTINEL
        redis_pass = settings.REDIS_PASS

        sentinel_addrs = redis_sentinel.split(",")
        sentinel_params = []

        # Single host, don't use Redis cluster
        if len(sentinel_addrs) == 1:
            host, port = sentinel_addrs[0].split(":")
            cls._sentinel = Redis(
                host=host, port=int(port), password=redis_pass, retry_on_timeout=True
            )
            return cls._sentinel

        # Use Redis Cluster Sentinel
        for addr in sentinel_addrs:
            host, port = addr.split(":")
            sentinel_params.append((host, int(port)))

        connection_kwargs = {
            "socket_timeout": 1.0,
            "retry_on_timeout": True,
            "socket_keepalive": True,
        }
        cls._sentinel = Sentinel(sentinel_params, **connection_kwargs)
        return cls._sentinel

    @classmethod
    def get_connect_pool(cls, host, port) -> BlockingConnectionPool:
        """Return connection pool to a Redis host

        If there is no pool to specific host, create a new one
        and save to use later.
        """
        pool_key = f"{host}:{port}"
        if pool_key in cls._pools:
            return cls._pools.get(pool_key)

        pool_kwargs = {
            "host": host,
            "port": port,
            "password": settings.REDIS_PASS,
            "max_connections": settings.REDIS_POOL_MAX_CONNECTIONS,
            "timeout": settings.REDIS_POOL_BLOCK_TIMEOUT,
            "health_check_interval": settings.REDIS_HEALTH_CHECK_INTERVAL,
            "socket_timeout": 1.0,
            "retry_on_timeout": True,
            "socket_keepalive": True,
        }
        pool = BlockingConnectionPool(**pool_kwargs)

        cls._pools[pool_key] = pool
        return pool

    @classmethod
    def get_master(cls) -> Redis:
        """
        Connection to redis master, using for write data
        """
        sentinel = cls.get_sentinel()
        if isinstance(sentinel, Redis):
            return sentinel

        host, port = sentinel.discover_master(settings.REDIS_DB_MASTER)
        master_pool = cls.get_connect_pool(host, port)
        return Redis(connection_pool=master_pool)

    @classmethod
    def get_slave(cls) -> Redis:
        """ Connection to redis slave, using for read data

        Using round-robin slave balancer
        """
        sentinel = cls.get_sentinel()
        if isinstance(sentinel, Redis):
            return sentinel

        slaves = sentinel.discover_slaves(settings.REDIS_DB_MASTER)
        if not slaves:
            return cls.get_master()

        # Round-robin balancer
        if cls._slave_rr_counter is None:
            cls._slave_rr_counter = random.randint(0, len(slaves))
        cls._slave_rr_counter = (cls._slave_rr_counter + 1) % len(slaves)

        host, port = slaves[cls._slave_rr_counter]
        slave_pool = cls.get_connect_pool(host, port)
        return Redis(connection_pool=slave_pool)


def get_master() -> Redis:
    """
    Connection to redis master, using for write data
    """
    return RedisManager.get_master()


def get_slave() -> Redis:
    """
    Connection to redis slave, using for read data
    """
    return RedisManager.get_slave()


def set_key(key: str, value: str, timeout: int = 0):
    """Set key-value with timeout in seconds

    If timeout == 0, key live forever.
    """
    master = get_master()
    if timeout:
        master.setex(key, timeout, value)
    else:
        master.set(key, value)


def set_key_dict(name: str, mapping: dict, timeout: int = 0):
    """
    Set key with value is Python dict, using HSET Redis.
    timeout in seconds
    """
    master = get_master()
    master.hset(name, mapping=mapping)
    if timeout:
        master.expire(name, timeout)


def get_key(name: str) -> dict:
    """Get object from name using HGETALL

    Return dict as value
    """
    return get_slave().hgetall(name)


def get_expired_time(key: str) -> int:
    """Get expired time of key
    """
    return get_master().ttl(key)


def set_key_raw(key: str, value: str):
    return get_master().set(key, value)


def get_key_raw(key: str):
    return get_slave().get(key)


def remove_key(key: str) -> None:
    master = get_master()
    return master.delete(key)


def save_access_token(token_key: str, expire_time: int, dict_payload: dict):
    """
    Save token data
    token_key: String Ex: 3be9bfe2881401369d6a2ec4ba609422
                          9411346bdca64813277d4beb550c1d5c
                          bdc3e87e0224d71f35e04ab8ab76af9a
                          3dd515906b57d246ec1c70b00911de51
    dict_payload: Dict Ex: {
        "login_id": "MT5_ID_EXAMPLE",
        "create_time": "2020-02-15 09:08:22.10293+00:00"
    }
    """
    master = get_master()
    master.hset(token_key, mapping=dict_payload)
    if expire_time:
        master.expire(token_key, expire_time)


def save_user_device(user_id: int, device_type: str, token_key: str):
    master = get_master()
    hash_key = consts.CACHED_KEY_DEVICE_USER.format(user_id=user_id)
    data = {"device_type": device_type, "token_key": token_key}
    master.hset(hash_key, mapping=data)


def check_user_device_type_exist(user_id: str, device_type: str) -> bool:
    slave = get_slave()
    hash_key = consts.CACHED_KEY_DEVICE_USER.format(user_id=user_id)

    old_device = slave.hget(hash_key, "device_type")
    return old_device == device_type.encode()
