import hubspot
from hubspot.crm.associations import BatchApi


def test_is_discoverable():
    apis = hubspot.Client.create().crm.associations
    assert isinstance(apis.batch_api, BatchApi)
