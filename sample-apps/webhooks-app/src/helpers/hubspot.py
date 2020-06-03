import hubspot
import os
from .oauth import refresh_and_get_access_token, is_authenticated


def create_client():
    if is_authenticated():
        return hubspot.Client.create(access_token=refresh_and_get_access_token())

    return hubspot.Client.create()
