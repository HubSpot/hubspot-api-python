from hubspot import HubSpot
from hubspot.crm.tickets import BasicApi, BatchApi, MergeApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.tickets
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.merge_api, MergeApi)
    assert isinstance(apis.search_api, SearchApi)
    assert hasattr(apis, "get_all")
