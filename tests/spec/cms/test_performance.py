from hubspot import HubSpot
from hubspot.cms.performance import DefaultApi


def test_is_discoverable():
    apis = HubSpot().cms.performance
    assert isinstance(apis.default_api, DefaultApi)
