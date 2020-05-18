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

WORKDIR /app/src

COPY ./sample-apps/webhooks-app/docker/web/supervisor.conf /etc/supervisor/conf.d/apache.conf

CMD ["/usr/bin/supervisord"]
#CMD ["python", "app.py"]
