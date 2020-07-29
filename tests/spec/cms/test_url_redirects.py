from hubspot import HubSpot
from hubspot.cms.url_redirects import RedirectsApi


def test_is_discoverable():
    apis = HubSpot().cms.url_redirects
    assert isinstance(apis.redirects_api, RedirectsApi)
