from hubspot import HubSpot
from hubspot.crm.properties import BatchApi, CoreApi, GroupsApi


def test_is_discoverable():
    apis = HubSpot().crm.properties
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.core_api, CoreApi)
    assert isinstance(apis.groups_api, GroupsApi)
