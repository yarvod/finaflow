from datetime import datetime, timedelta

import jwt
import redis
from django.conf import settings
from users.models import User


# Redis connection
redis_con = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASS,
    db=1,
)


def check_user(**kwargs) -> tuple:
    user = User.objects.filter(**kwargs).only("is_active").first()
    if user is not None and user.is_active:
        return user, True
    else:
        return None, False


def generate_access_token(user: User) -> str:
    access_token_payload = {
        "user_id": str(user.id),
        "exp": datetime.utcnow() + timedelta(days=0, minutes=15),
        "iat": datetime.utcnow(),
    }
    access_token = jwt.encode(
        access_token_payload, settings.JWT_SECRET, algorithm="HS256"
    )
    return access_token


def generate_refresh_token(user: User) -> str:
    refresh_token_payload = {
        "user_id": str(user.id),
        "exp": datetime.utcnow() + timedelta(days=7),
        "iat": datetime.utcnow(),
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.JWT_SECRET, algorithm="HS256"
    )
    return refresh_token


def get_refresh_token(user_id: str, token: str) -> bool:
    r = redis_con.sismember(f"{user_id}:devices:tokens", token)
    return bool(r)


def set_refresh_token(user_id: str, token: str) -> bool:
    r = redis_con.sadd(f"{user_id}:devices:tokens", token)
    return bool(r)


def remove_refresh_token(user_id: str, token: str) -> bool:
    r = redis_con.srem(f"{user_id}:devices:tokens", token)
    return bool(r)


def remove_all_tokens(user_id: str) -> bool:
    r = redis_con.delete(f"{user_id}:devices:tokens")
    return bool(r)
