from hubspot import HubSpot
from hubspot.crm.objects.postal_mail import BasicApi, BatchApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.objects.postal_mail
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
