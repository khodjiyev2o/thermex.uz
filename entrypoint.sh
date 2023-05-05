#!/bin/sh
source venv/bin/activate
pip install -r requirements/prod.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000
exec "$@"