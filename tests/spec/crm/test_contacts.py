from hubspot import HubSpot
from hubspot.crm.contacts import BasicApi, BatchApi, GDPRApi, MergeApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.contacts
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.gdpr_api, GDPRApi)
    assert isinstance(apis.merge_api, MergeApi)
    assert isinstance(apis.search_api, SearchApi)
    assert hasattr(apis, "get_all")
