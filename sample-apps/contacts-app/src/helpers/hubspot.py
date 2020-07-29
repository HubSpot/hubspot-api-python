import os
from hubspot import HubSpot
from .oauth import refresh_and_get_access_token, is_authorized


def create_client():
    if is_authorized():
        return HubSpot(access_token=refresh_and_get_access_token())
    api_key = os.environ.get("HUBSPOT_API_KEY")
    if api_key is not None:
        return HubSpot(api_key=api_key)

    return HubSpot()
