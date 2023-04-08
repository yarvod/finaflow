import string
import random
import redis
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from users.models import User


# Redis connection
redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASS,
    db=1,
)


def verify_token(email_token: str, user: User) -> bool:
    """Return token verification result"""
    try:
        valid = default_token_generator.check_token(user, email_token)
        if valid:
            return True
        else:
            return False
    except Exception:
        return False


def set_hash_with_ttl(user_id: str, my_hash: str, ttl: int) -> bool:
    redis_instance.hset(user_id, "hash", my_hash)
    redis_instance.expire(name=user_id, time=ttl)
    return True


def get_user_hash(user_id: str) -> str:
    result = redis_instance.hget(user_id, "hash")
    if result:
        return str(result, "UTF-8")
    return "Not Found"


def delete_hash(user_id: str) -> bool:
    result = redis_instance.hdel(user_id, "hash")
    return bool(result)


def gen_random_string(length: int) -> str:
    return "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits + "@#$%*&-!")
        for _ in range(length)
    )


def check_user(**kwargs):
    user = User.objects.filter(**kwargs).only("is_active").first()
    if user is None or user.is_active is True:
        return True
    else:
        return False
