#!/bin/sh
source venv/bin/activate
pip3 install -r requirements/prod.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000
exec "$@"

