from flask import Blueprint, request
import json
import os
from services.kafka import get_producer
from auth import hubspot_signature_required


module = Blueprint("webhooks", __name__)


@module.route("/handle", methods=["POST"])
@hubspot_signature_required
def handle():
    events = json.loads(request.data)
    producer = get_producer()
    for event in events:
        producer.send(os.getenv("EVENTS_TOPIC"), value=event)

    return "", 204
