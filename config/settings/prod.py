from .base import *  # noqa
import sys

DEBUG = True
ALLOWED_HOSTS = ["18.228.10.255", "127.0.0.1", "api.san-neo.uz"]
CORS_ORIGIN_ALLOW_ALL = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    },
}
if "test" not in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
