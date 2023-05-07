FROM  --platform=linux/amd64 python:3.8

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1


COPY ./requirements/base.txt  .
COPY ./requirements/prod.txt  .

# install dependencies


RUN pip install --upgrade pip
RUN pip install -r prod.txt



COPY ./ .

RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
CMD ["/usr/src/app/entrypoint.sh"]