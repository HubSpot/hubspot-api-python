from os import getenv
import urllib.parse
from flask import request
from functools import wraps
from hubspot.exceptions import InvalidSignatureError
from hubspot.utils.webhooks import validate_signature


def hubspot_signature_required(func):
    @wraps(func)
    def _validate_signature(*args, **kwargs):
        try:
            validate_signature(
                signature=request.headers["X-HubSpot-Signature"],
                signature_version=request.headers["X-HubSpot-Signature-Version"],
                http_uri=urllib.parse.unquote(request.url),
                http_method=request.method,
                request_body=request.data.decode("utf-8"),
                client_secret=getenv("HUBSPOT_CLIENT_SECRET"),
            )
            return func(*args, **kwargs)
        except InvalidSignatureError:
            return "", 403

    return _validate_signature
