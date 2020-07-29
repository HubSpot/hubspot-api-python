from hubspot import HubSpot
from hubspot.crm.line_items import BatchApi, SearchApi, BasicApi


def test_is_discoverable():
    apis = HubSpot().crm.line_items
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
