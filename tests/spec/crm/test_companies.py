from hubspot import HubSpot
from hubspot.crm.companies import BasicApi, AssociationsApi, BatchApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.companies
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.associations_api, AssociationsApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
    assert hasattr(apis, "get_all")
