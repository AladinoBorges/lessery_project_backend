FROM python:3.11.1-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
  && pip install pipenv
COPY ../Pipfile .
COPY ../Pipfile.lock .
RUN pipenv install --deploy --system

COPY . .