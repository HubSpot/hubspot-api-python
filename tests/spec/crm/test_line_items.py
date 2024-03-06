from hubspot import HubSpot
from hubspot.crm.line_items import BatchApi, GDPRApi, BasicApi, SearchApi, PublicObjectApi


def test_is_discoverable():
    apis = HubSpot().crm.line_items
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.gdpr_api, GDPRApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
    assert isinstance(apis.public_object_api, PublicObjectApi)
