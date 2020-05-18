from flask import Blueprint, request
import json
import os
from services.kafka import get_producer


module = Blueprint("webhooks", __name__)


@module.route("/handle", methods=["POST"])
def handle():
    data = request.data
    events = json.loads(data)
    producer = get_producer()
    for event in events:
        producer.send(os.getenv("EVENTS_TOPIC"), value=event)

    return "", 204
