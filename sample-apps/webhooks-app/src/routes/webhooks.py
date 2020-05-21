from flask import Blueprint, request
import json
import os
from services.kafka import get_producer
from hubspot.utils.webhooks import validate_signature
from hubspot.exceptions import InvalidSignatureError


module = Blueprint("webhooks", __name__)


@module.route("/handle", methods=["POST"])
def handle():
    try:
        validate_signature(
            signature=request.headers['X-HubSpot-Signature'],
            signature_version=request.headers['X-HubSpot-Signature-Version'],
            http_uri=request.base_url,
            request_body=request.data.decode("utf-8"),
            client_secret=os.getenv("HUBSPOT_CLIENT_SECRET"),
        )
    except InvalidSignatureError:
        return "", 403

    events = json.loads(request.data)
    producer = get_producer()
    for event in events:
        producer.send(os.getenv("EVENTS_TOPIC"), value=event)

    return "", 204
