from hubspot import HubSpot
from hubspot.crm.lists import ListAppApi, ListAppMembershipApi


def test_is_discoverable():
    apis = HubSpot().crm.lists
    assert isinstance(apis.list_app_api, ListAppApi)
    assert isinstance(apis.list_app_membership_api, ListAppMembershipApi)

