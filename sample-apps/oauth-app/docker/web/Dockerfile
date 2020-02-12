FROM python:3.8

RUN mkdir -p /app
ADD ./sample-apps/oauth-app/requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

WORKDIR /app/src
CMD python app.py
