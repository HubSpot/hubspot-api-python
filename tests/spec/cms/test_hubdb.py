from hubspot import HubSpot
from hubspot.cms.hubdb import DefaultApi


def test_is_discoverable():
    apis = HubSpot().cms.hubdb
    assert isinstance(apis.default_api, DefaultApi)
