FROM python:3.8

RUN mkdir -p /sdk
ADD ./hubspot /sdk/hubspot
ADD ./setup.py VERSION /sdk/
WORKDIR /sdk
RUN pip install -e .

RUN mkdir -p /app
ADD ./sample-apps/trello-integration-app/requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

# dockerize
ENV DOCKERIZE_VERSION v0.6.1
ADD https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz /tmp
RUN tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /app/src
