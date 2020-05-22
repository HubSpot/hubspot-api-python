import hubspot
import os
from .oauth import refresh_and_get_access_token, is_authenticated


def create_client():
    if is_authenticated():
        return hubspot.Client.create(access_token=refresh_and_get_access_token())

    return hubspot.Client.create()


def create_client_with_developer_api_key():
    return hubspot.Client.create(api_key=os.getenv("HUBSPOT_DEVELOPER_API_KEY"))
