from hubspot import HubSpot
from hubspot.crm.lists import ListsApi, MembershipsApi


def test_is_discoverable():
    apis = HubSpot().crm.lists
    assert isinstance(apis.lists_api, ListsApi)
    assert isinstance(apis.memberships_api, MembershipsApi)

