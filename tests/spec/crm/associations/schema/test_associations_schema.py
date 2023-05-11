from hubspot import HubSpot
from hubspot.crm.associations.schema import TypesApi


def test_is_discoverable():
    apis = HubSpot().crm.associations.schema
    assert isinstance(apis.types_api, TypesApi)
