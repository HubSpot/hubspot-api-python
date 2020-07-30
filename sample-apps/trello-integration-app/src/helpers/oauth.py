from os import getenv
from hubspot import HubSpot
from datetime import datetime, timedelta
from flask import request
from repositories import SettingsRepository


def save_tokens_response(tokens_response):
    return SettingsRepository.save_tokens(
        access_token=tokens_response.access_token,
        refresh_token=tokens_response.refresh_token,
        expires_in=tokens_response.expires_in,
        expires_at=datetime.now()
        + timedelta(seconds=tokens_response.expires_in * 0.95),
    )


def is_authorized():
    settings = SettingsRepository.find_one()
    return settings.refresh_token is not None


def get_redirect_uri():
    return request.url_root + "oauth/callback"


def refresh_and_get_access_token():
    if not is_authorized():
        raise Exception("No refresh token is specified")
    settings = SettingsRepository.find_one()
    if datetime.now() > settings.token_expires_at:
        tokens_response = HubSpot().auth.oauth.default_api.create_token(
            grant_type="refresh_token",
            refresh_token=settings.refresh_token,
            client_id=getenv("HUBSPOT_CLIENT_ID"),
            client_secret=getenv("HUBSPOT_CLIENT_SECRET"),
        )
        settings = save_tokens_response(tokens_response)

    return settings.access_token
