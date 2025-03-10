from hubspot import HubSpot
from hubspot.crm.schemas import CoreApi


def test_is_discoverable():
    apis = HubSpot().crm.schemas
    assert isinstance(apis.core_api, CoreApi)
