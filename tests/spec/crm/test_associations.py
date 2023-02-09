from hubspot import HubSpot
from hubspot.crm.associations import BatchApi, TypesApi


def test_is_discoverable():
    apis = HubSpot().crm.associations
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.types_api, TypesApi)
