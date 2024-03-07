from hubspot import HubSpot
from hubspot.crm.objects.emails import BasicApi, BatchApi, GDPRApi, PublicObjectApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.objects.emails
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.gdpr_api, GDPRApi)
    assert isinstance(apis.public_object_api, PublicObjectApi)
    assert isinstance(apis.search_api, SearchApi)
