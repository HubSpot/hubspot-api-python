import os
import hubspot
from .oauth import refresh_and_get_access_token, is_authenticated


def create_client():
    api_key = os.environ.get('HUBSPOT_API_KEY')
    if is_authenticated():
        return hubspot.Client.create(access_token=refresh_and_get_access_token())
    if api_key is not None:
        return hubspot.Client.create(api_key=api_key)

    return hubspot.Client.create()
