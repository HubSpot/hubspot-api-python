from hubspot import HubSpot
from hubspot.crm.associations.v4 import BatchApi, DefinitionsApi


def test_is_discoverable():
    apis = HubSpot().crm.associations.v4
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.definitions_api, DefinitionsApi)
