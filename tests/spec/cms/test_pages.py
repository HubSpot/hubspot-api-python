from hubspot import HubSpot
from hubspot.cms.pages import LandingPagesApi, SitePagesApi


def test_is_discoverable():
    apis = HubSpot().cms.pages
    assert isinstance(apis.landing_pages_api, LandingPagesApi)
    assert isinstance(apis.site_pages_api, SitePagesApi)
