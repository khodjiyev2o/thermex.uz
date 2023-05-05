FROM python:3.9.2-alpine
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV DJANGO_SETTINGS_MODULE=config.settings.base
COPY requirements/prod.txt prod.txt
COPY requirements/base.txt base.txt

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r prod.txt

COPY ./ .
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput