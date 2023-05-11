#!/bin/sh

python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py populate
django-admin compilemessages --ignore=env
exec "$@"