import hubspot
from hubspot.cms.site_search import DefaultApi


def test_is_discoverable():
    apis = hubspot.Client.create().cms.site_search
    assert isinstance(apis.default_api, DefaultApi)
