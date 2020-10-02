from hubspot import HubSpot
from hubspot.crm.schemas import DefaultApi, CoreApi


def test_is_discoverable():
    apis = HubSpot().crm.schemas
    assert isinstance(apis.default_api, DefaultApi)
    assert isinstance(apis.core_api, CoreApi)
