FROM python:3.8

RUN apt-get update && apt-get install -y supervisor

RUN mkdir -p /sdk
ADD ./hubspot /sdk/hubspot
ADD ./setup.py /sdk
WORKDIR /sdk
RUN pip install -e .

RUN mkdir -p /app
ADD ./sample-apps/webhooks-app/requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install watchdog pyyaml argh

COPY ./sample-apps/webhooks-app/docker/web/supervisor.conf /etc/supervisor/conf.d/apache.conf

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /app/src
