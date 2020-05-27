FROM python:3.8

RUN mkdir -p /sdk
ADD ./hubspot /sdk/hubspot
ADD ./setup.py VERSION /sdk/
WORKDIR /sdk
RUN pip install -e .

RUN mkdir -p /app
ADD ./sample-apps/oauth-app/requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

WORKDIR /app/src
CMD python app.py
