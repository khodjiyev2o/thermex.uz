from .base import *  # noqa


DEBUG = True
ALLOWED_HOSTS = ["95.130.227.48", "127.0.0.1", "api.san-neo.uz", "thermexuz.uz"]
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
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
ADMINS = [
    ("Admin Name", env.str("DEFAULT_EMAIL")),
]
SERVER_EMAIL = env.str("DEFAULT_EMAIL")
