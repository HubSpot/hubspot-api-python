from hubspot import HubSpot
from hubspot.discovery.cms.blogs.discovery import Discovery


def test_is_discoverable():
    apis = HubSpot().cms
    assert isinstance(apis.blogs, Discovery)
