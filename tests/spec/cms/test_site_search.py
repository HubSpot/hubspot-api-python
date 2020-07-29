from hubspot import HubSpot
from hubspot.cms.site_search import DefaultApi


def test_is_discoverable():
    apis = HubSpot().cms.site_search
    assert isinstance(apis.default_api, DefaultApi)
