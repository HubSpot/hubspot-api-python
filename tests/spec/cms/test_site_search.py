from hubspot import HubSpot
from hubspot.cms.site_search import PublicApi


def test_is_discoverable():
    apis = HubSpot().cms.site_search
    assert isinstance(apis.public_api, PublicApi)
