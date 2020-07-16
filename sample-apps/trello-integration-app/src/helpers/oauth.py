from os import getenv
import hubspot
from datetime import datetime, timedelta
from flask import request
from repositories.tokens import save_token, get_token


def save_token_response(tokens_response):
    return save_token(
        access_token=tokens_response.access_token,
        refresh_token=tokens_response.refresh_token,
        expires_in=tokens_response.expires_in,
        expires_at=datetime.now() + timedelta(
            seconds=tokens_response.expires_in * 0.95
        ),
    )


def is_authorized():
    token = get_token()
    return token is not None


def get_redirect_uri():
    return request.url_root + "oauth/callback"


def refresh_and_get_access_token():
    if not is_authorized():
        raise Exception("No refresh token is specified")
    token = get_token()
    if datetime.now() > token.expires_at:
        token_response = hubspot.Client.create().auth.oauth.default_api.create_token(
            grant_type="refresh_token",
            refresh_token=token.refresh_token,
            client_id=getenv("HUBSPOT_CLIENT_ID"),
            client_secret=getenv("HUBSPOT_CLIENT_SECRET"),
        )
        token = save_token_response(token_response)

    return token.access_token
