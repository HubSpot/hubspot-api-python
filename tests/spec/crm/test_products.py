from hubspot import HubSpot
from hubspot.crm.products import BasicApi, AssociationsApi, BatchApi, SearchApi, PublicObjectApi


def test_is_discoverable():
    apis = HubSpot().crm.products
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.associations_api, AssociationsApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
    assert isinstance(apis.public_object_api, PublicObjectApi)
    assert hasattr(apis, "get_all")
