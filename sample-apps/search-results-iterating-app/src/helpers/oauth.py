import time
import os
import json
from flask import request
from hubspot import HubSpot
from services.redis import redis

TOKENS_KEY = "tokens"


def save_tokens(tokens_response):
    tokens = {
        "access_token": tokens_response.access_token,
        "refresh_token": tokens_response.refresh_token,
        "expires_in": tokens_response.expires_in,
        "expires_at": time.time() + tokens_response.expires_in * 0.95,
    }
    redis.set(TOKENS_KEY, json.dumps(tokens))

    return tokens


def is_authorized():
    return redis.exists(TOKENS_KEY)


def get_redirect_uri():
    return request.url_root + "oauth/callback"


def refresh_and_get_access_token():
    if not is_authorized():
        raise Exception("No refresh token is specified")
    tokens = json.loads(redis.get(TOKENS_KEY))
    if time.time() > tokens["expires_at"]:
        tokens = HubSpot().auth.oauth.default_api.create_token(
            grant_type="refresh_token",
            refresh_token=tokens["refresh_token"],
            client_id=os.environ.get("HUBSPOT_CLIENT_ID"),
            client_secret=os.environ.get("HUBSPOT_CLIENT_SECRET"),
        )
        tokens = save_tokens(tokens)

    return tokens["access_token"]
