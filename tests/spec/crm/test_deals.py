from hubspot import HubSpot
from hubspot.crm.deals import BasicApi, BatchApi, GDPRApi, SearchApi, PublicObjectApi


def test_is_discoverable():
    apis = HubSpot().crm.deals
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.gdpr_api, GDPRApi)
    assert isinstance(apis.search_api, SearchApi)
    assert isinstance(apis.public_object_api, PublicObjectApi)
    assert hasattr(apis, "get_all")
