import hubspot
from .oauth import refresh_and_get_access_token, is_authorized
from urllib3.util.retry import Retry


def create_client():
    if is_authorized():
        retry = Retry(total=3, backoff_factor=2, status_forcelist=(429, 500, 502, 504),)
        return hubspot.Client.create(
            access_token=refresh_and_get_access_token(), retry=retry
        )

    return hubspot.Client.create()
