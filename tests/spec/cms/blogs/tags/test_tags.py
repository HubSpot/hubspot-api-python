from hubspot import HubSpot
from hubspot.cms.blogs.tags import TagApi


def test_is_discoverable():
    apis = HubSpot().cms.blogs.tags
    assert isinstance(apis.tag_api, TagApi)
