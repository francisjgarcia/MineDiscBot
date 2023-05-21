FROM python:3.11.2-alpine3.17

LABEL maintainer Francis J. Garcia <contacto@francisjgarcia.es>
LABEL org.opencontainers.image.source="https://github.com/francisjgarcia/minediscbot"
LABEL org.opencontainers.image.description "App written in Python to update the status of a Minecraft server in Discord using mineapi API"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN addgroup -S python && adduser -S python -G python

USER python:python

WORKDIR /usr/src/app

COPY --chown=python:python app .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "-u", "app.py" ]
