FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y mc postgresql python-psycopg2 libpq-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm -rf /var/cache/apt
