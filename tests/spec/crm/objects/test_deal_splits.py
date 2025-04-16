from hubspot import HubSpot
from hubspot.crm.objects.deal_splits import BatchApi


def test_is_discoverable():
    apis = HubSpot().crm.objects.deal_splits
    assert isinstance(apis.batch_api, BatchApi)
