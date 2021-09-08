from hubspot import HubSpot
from hubspot.crm.objects import BasicApi, AssociationsApi, BatchApi, SearchApi, GDPRApi


def test_is_discoverable():
    apis = HubSpot().crm.objects
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.associations_api, AssociationsApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
    assert isinstance(apis.gdpr_api, GDPRApi)
