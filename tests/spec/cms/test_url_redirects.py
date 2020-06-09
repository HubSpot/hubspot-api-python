import hubspot
from hubspot.cms.url_redirects import RedirectsApi


def test_is_discoverable():
    apis = hubspot.Client.create().cms.url_redirects
    assert isinstance(apis.redirects_api, RedirectsApi)
