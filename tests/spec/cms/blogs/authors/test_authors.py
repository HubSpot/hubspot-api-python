from hubspot import HubSpot
from hubspot.cms.blogs.authors import BlogAuthorsApi


def test_is_discoverable():
    apis = HubSpot().cms.blogs.authors
    assert isinstance(apis.author_api, BlogAuthorsApi)
