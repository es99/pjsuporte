FROM python:3.9-alpine3.15

LABEL maintainer="Engels Souza - Sysadmin Infopublic <engels.franca@gmail.com>"

ENV FLASK_APP flasky.py
ENV FLASK_CONFIG docker

RUN apk add gcc && apk add g++ && apk add libffi-dev

RUN adduser -D flasky
USER flasky

WORKDIR /home/flasky

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements/docker.txt

COPY infopublic_usuarios infopublic_usuarios
COPY migrations migrations
COPY flasky.py config.py boot.sh ./

EXPOSE 8000

ENTRYPOINT [ "./boot.sh" ]