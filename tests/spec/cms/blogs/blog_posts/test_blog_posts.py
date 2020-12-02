from hubspot import HubSpot
from hubspot.cms.blogs.blog_posts import DefaultApi


def test_is_discoverable():
    apis = HubSpot().cms.blogs.blog_posts
    assert isinstance(apis.default_api, DefaultApi)
