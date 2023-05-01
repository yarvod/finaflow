import sys
from datetime import timedelta
from pathlib import Path
import os

from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = ["*"]
HOST = os.environ.get("HOST")
HTTP = os.environ.get("HTTP")

# Application definition

INSTALLED_APPS = [
    # 'jet',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "psycopg2",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "django_extensions",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.yandex",
    "django_filters",
    "ckeditor",
    "storages",
    "drf_api_logger",
    "drf_yasg",
    "users",
    "authentication",
    "common",
    "finances",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware",
]

ROOT_URLCONF = "backend_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend_app.wsgi.application"
DRF_API_LOGGER_DATABASE = True

# Database

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("POSTGRES_DB", "postgres"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("DB_HOST", "postgres"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

if "test" in sys.argv:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test_db.sqlite3",
    }

# REDIS SETTINGS

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_PASS = os.environ.get("REDIS_PASSWORD", "redis")

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# CACHE

CACHE_REDIS = True
if CACHE_REDIS:
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
    DEFAULT_CACHE_TTL = 10
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": f"redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}/0",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "unique - snowflake",
        }
    }

TEST_CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# Static

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Media

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

MEDIA_PREFIX = f"{HTTP}://{HOST}" if DEBUG else ""

TEST_DIR = "test_data"

# File upload settings
CONTENT_TYPES = ["image"]
MAX_UPLOAD_SIZE = 5242880

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "authentication.authenticate.CustomAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    # 'DEFAULT_RENDERER_CLASSES': (
    #          'rest_framework.renderers.JSONRenderer',
    #      )
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
    ],
}

# smtp
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.yandex.com"
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587

EMAIL_INVITE_EMPLOYER_URL = "%s://%s/account/invite/{uid}/{token}/{company_uid}" % (
    HTTP,
    HOST,
)
EMAIL_ACTIVATION_URL = "%s://%s/account/activate/{uid}/{token}" % (HTTP, HOST)
EMAIL_RESET_PASSWORD_URL = "%s://%s/account/password-reset/{uid}/{token}" % (HTTP, HOST)
EMAIL_SHOW_RESUME_URL = "%s://%s/resumes/{id}/details" % (HTTP, HOST)
EMAIL_SHOW_VACANCY_URL = "%s://%s/vacancies/{id}/details" % (HTTP, HOST)

AUTH_USER_MODEL = "users.User"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=int(os.getenv("ACCESS_TOKEN_LIFETIME", 5))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=int(os.getenv("REFRESH_TOKEN_LIFETIME", 3))
    ),
    "ROTATE_REFRESH_TOKENS": True,
    "ALGORITHM": "HS512",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("JWT",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

JWT_AUTH_COOKIE = "access_token"
JWT_AUTH_SECURE = False
JWT_AUTH_REFRESH_COOKIE = "refresh_token"
AUTH_COOKIE_HTTP_ONLY = True
JWT_AUTH_COOKIE_PATH = "/"
JWT_AUTH_REFRESH_COOKIE_PATH = "/api/auth/"
AUTH_COOKIE_SAMESITE = "Lax"
JWT_AUTH_COOKIE_USE_CSRF = True  # Must be True for production! (as I understand)
# "True" entails comparison of X-CSRFToken in header with csrftoken in cookie
# "True" requires frontend's guys to set Header "X-CSRFToken" from cookie "csrftoken"
# For details look into CsrfViewMiddleware.process_view or on django github
# (https://github.com/django/django/blob/22916c8c1f9648931344c7f77fe9f71069dc5765/django/middleware/csrf.py#L294-L313)

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "offline",
        },
        "APP": {
            "client_id": os.environ.get("GOOGLE_OAUTH2_CLIENT_ID"),
            "secret": os.environ.get("GOOGLE_OAUTH2_SECRET"),
            "key": "",
        },
    },
    "yandex": {
        "APP": {
            "client_id": os.environ.get("YANDEX_OAUTH2_CLIENT_ID"),
            "secret": os.environ.get("YANDEX_OAUTH2_SECRET"),
            "key": "",
        }
    },
}

YANDEX_OAUTH2_REDIRECT = os.environ.get("YANDEX_OAUTH2_REDIRECT")
GOOGLE_OAUTH2_REDIRECT = os.environ.get("GOOGLE_OAUTH2_REDIRECT")

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

ACCOUNT_ADAPTER = "authentication.adapters.CustomAccountAdapter"

REST_USE_JWT = True
REST_AUTH_SERIALIZERS = {
    "JWT_TOKEN_CLAIMS_SERIALIZER": "authentication.serializers.CookieTokenObtainSerializer"
}

# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    f"http://localhost:8080",
    f"http://localhost:8100",
    f"{HTTP}://{HOST}",
    f"capacitor://finaflow.ru",
    f"capacitor://localhost",
]
# X_FRAME_OPTIONS = "SAMEORIGIN"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(levelname) -4s %(name) -2s [%(pathname)s:%(lineno)d] %(message)s"
        },
        "file": {
            "format": "%(asctime)s %(levelname) -4s %(name) -2s [%(filename)s:%(lineno)d] %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": f"{BASE_DIR}/total.log",
        },
    },
    "loggers": {
        "": {"level": "INFO", "handlers": ["console", "file"]},
    },
}

# Celery

CELERY_BROKER_URL = "redis://:{}@{}:{}/2".format(REDIS_PASS, REDIS_HOST, REDIS_PORT)
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "exportpdf",
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline"],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
    }
}

# STORAGE

YANDEX_BUCKET_NAME = os.environ.get("YANDEX_BUCKET_NAME")
AWS_S3_ACCESS_KEY_ID = os.environ.get("YANDEX_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = os.environ.get("YANDEX_SECRET_ACCESS_KEY")
AWS_S3_ENDPOINT_URL = "https://storage.yandexcloud.net"
AWS_S3_REGION_NAME = os.environ.get("YANDEX_BUCKET_NAME")

USE_S3 = os.getenv("USE_S3", "false").lower() == "true"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
if USE_S3:
    DEFAULT_FILE_STORAGE = "backend_app.storage.HashedFilenameS3Boto3Storage"
