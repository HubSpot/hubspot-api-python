from hubspot import HubSpot
from hubspot.crm.commerce.invoices import BasicApi, BatchApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.commerce.invoices
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
    assert hasattr(apis, "get_all")
