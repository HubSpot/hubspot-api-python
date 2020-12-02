from hubspot import HubSpot
from hubspot.cms.blogs.authors import DefaultApi


def test_is_discoverable():
    apis = HubSpot().cms.blogs.authors
    assert isinstance(apis.default_api, DefaultApi)
