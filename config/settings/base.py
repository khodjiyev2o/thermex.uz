import os
from datetime import timedelta
from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _
from firebase_admin import initialize_app


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# READING ENV
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))


SECRET_KEY = env.str("SECRET_KEY")
DEBUG = True


ALLOWED_HOSTS = ["*"]

LOCAL_APPS = [
    "apps.users.apps.UsersConfig",
    "apps.common.apps.CommonConfig",
    "apps.products.apps.ProductsConfig",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "phonenumber_field",
    "drf_yasg",
    "fcm_django",
]
DJANGO_APPS = [
    "jazzmin",
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
AUTH_USER_MODEL = "users.User"
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True
USE_L10N = True


STATIC_URL = "staticfiles/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (BASE_DIR / "static",)

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

JAZZMIN_SETTINGS = {
    "site_brand": "THERMEX",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "thermex.jpg",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "thermex.jpg",
    "site_logo_classes": "img-circle",
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=99),
}

MODELTRANSLATION_LANGUAGES = ("uz", "ru")
MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"

LANGUAGES = (
    ("uz", _("Uzbek")),
    ("ru", _("Russian")),
)
MODELTRANSLATION_LANGUAGES_CHOICES = (
    ("uz", _("Uzbek")),
    ("ru", _("Russian")),
)
MODELTRANSLATION_FALLBACK_LANGUAGES = ("uz", "ru")

LOCALE_PATHS = [
    BASE_DIR / "locale/",
]


FIREBASE_APP = initialize_app()


FCM_DJANGO_SETTINGS = {
    "DEFAULT_FIREBASE_APP": None,
    "APP_VERBOSE_NAME": _("Devices"),
    "ONE_DEVICE_PER_USER": False,
    "DELETE_INACTIVE_DEVICES": False,
}
