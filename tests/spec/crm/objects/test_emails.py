from hubspot import HubSpot
from hubspot.crm.objects.emails import BasicApi, BatchApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.objects.emails
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
