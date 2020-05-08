import hubspot
from hubspot.auth.oauth import DefaultApi


def test_is_discoverable():
    apis = hubspot.Client.create().auth.oauth
    assert isinstance(apis.default_api, DefaultApi)
