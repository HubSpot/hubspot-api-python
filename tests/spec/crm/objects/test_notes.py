from hubspot import HubSpot
from hubspot.crm.objects.notes import BasicApi, BatchApi, SearchApi, PublicObjectApi


def test_is_discoverable():
    apis = HubSpot().crm.objects.notes
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
    assert isinstance(apis.public_object_api, PublicObjectApi)
