from hubspot import HubSpot
from hubspot.auth.oauth import DefaultApi


def test_is_discoverable():
    apis = HubSpot().auth.oauth
    assert isinstance(apis.default_api, DefaultApi)
