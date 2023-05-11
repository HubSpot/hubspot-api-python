from hubspot import HubSpot
from hubspot.crm.associations import BatchApi


def test_is_discoverable():
    apis = HubSpot().crm.associations
    assert isinstance(apis.batch_api, BatchApi)
    assert hasattr(apis, "v4")
    assert hasattr(apis, "schema")
