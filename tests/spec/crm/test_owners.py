from hubspot import HubSpot
from hubspot.crm.owners import OwnersApi


def test_is_discoverable():
    apis = HubSpot().crm.owners
    assert isinstance(apis.owners_api, OwnersApi)
    assert hasattr(apis, "get_all")
