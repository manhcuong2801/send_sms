from django.utils import timezone

from apps.core.redis_service import save_access_token
from apps.users.utils import generate_access_key, get_expired_time_access_token

UNIT_TEST_META_SUCCESS = {"code": 200, "message": "success"}


def unit_test_generate_key():
    access_key = generate_access_key()
    now = timezone.now()
    expire_time = get_expired_time_access_token(now, "Mobile")
    redis_payload = {
        "login_id": "deadpool@example.com",
        "user": "500",
        "device_type": "Mobile",
    }
    save_access_token(access_key, expire_time[1], redis_payload)
    return access_key
