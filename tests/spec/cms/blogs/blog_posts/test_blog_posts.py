from hubspot import HubSpot
from hubspot.cms.blogs.blog_posts import BasicApi, BatchApi, MultiLanguageApi


def test_is_discoverable():
    apis = HubSpot().cms.blogs.blog_posts
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.multi_language_api, MultiLanguageApi)
