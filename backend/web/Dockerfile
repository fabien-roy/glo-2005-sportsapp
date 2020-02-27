FROM python:3.8.1
MAINTAINER Fabien Roy <fabienroy28@gmail.com>

RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

RUN mkdir -p /home/flask/app/web
WORKDIR /home/flask/app/web

COPY requirements.txt /home/flask/app/web
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/flask/app/web

RUN chown -R flask:flaskgroup /home/flask

USER flask
