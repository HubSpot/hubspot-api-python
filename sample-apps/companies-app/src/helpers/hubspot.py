from hubspot import HubSpot
from .oauth import refresh_and_get_access_token, is_authorized


def create_client():
    if is_authorized():
        return HubSpot(access_token=refresh_and_get_access_token())

    return HubSpot()
