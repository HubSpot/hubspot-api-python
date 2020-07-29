from hubspot import HubSpot
from hubspot.crm.owners import DefaultApi


def test_is_discoverable():
    apis = HubSpot().crm.owners
    assert isinstance(apis.default_api, DefaultApi)
    assert hasattr(apis, "get_all")
