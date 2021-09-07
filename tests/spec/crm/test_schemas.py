from hubspot import HubSpot
from hubspot.crm.schemas import PublicObjectSchemasApi, CoreApi


def test_is_discoverable():
    apis = HubSpot().crm.schemas
    assert isinstance(apis.public_object_schemas_api, PublicObjectSchemasApi)
    assert isinstance(apis.core_api, CoreApi)
