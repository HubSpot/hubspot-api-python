from hubspot import HubSpot
from hubspot.marketing.transactional import DefaultApi


def test_is_discoverable():
    apis = HubSpot().marketing.transactional 
    assert isinstance(apis.default_api, DefaultApi)
