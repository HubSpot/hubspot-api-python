from hubspot import HubSpot
from hubspot.crm.objects.feedback_submissions import BasicApi, AssociationsApi, BatchApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.objects.feedback_submissions
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.associations_api, AssociationsApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
