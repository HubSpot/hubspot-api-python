from os import getenv
from hubspot import HubSpot
from .oauth import refresh_and_get_access_token, is_authorized


def create_client():
    if is_authorized():
        return HubSpot(access_token=refresh_and_get_access_token())

    return HubSpot()


def create_client_with_developer_api_key():
    return HubSpot(api_key=getenv("HUBSPOT_DEVELOPER_API_KEY"))
