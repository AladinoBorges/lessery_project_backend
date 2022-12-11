FROM python:3.11.1-slim-bullseye

WORKDIR /usr/src/api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
  && pip install pipenv
COPY ../Pipfile .
COPY ../Pipfile.lock .
RUN pipenv install --deploy --system

COPY . .

# entrypoint
COPY ./local-entrypoint.sh /usr/src/api/local-entrypoint.sh
RUN chmod +x /usr/src/api/local-entrypoint.sh

CMD ["/bin/bash", "-c", "./local-entrypoint.sh"]