from hubspot import HubSpot
from hubspot.cms.blogs.tags import DefaultApi


def test_is_discoverable():
    apis = HubSpot().cms.blogs.tags
    assert isinstance(apis.default_api, DefaultApi)
