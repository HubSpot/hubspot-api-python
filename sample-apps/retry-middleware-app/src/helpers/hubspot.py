import hubspot
from .oauth import refresh_and_get_access_token, is_authenticated
from urllib3.util.retry import Retry


def create_client():
    if is_authenticated():
        return hubspot.Client.create(access_token=refresh_and_get_access_token())

    return hubspot.Client.create()
