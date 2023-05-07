from .base import *
DEBUG = True
ALLOWED_HOSTS = ['18.228.10.255', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'sammy',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}
