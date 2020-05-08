import hubspot
from hubspot.crm.imports import CoreApi


def test_is_discoverable():
    apis = hubspot.Client.create().crm.imports
    assert isinstance(apis.core_api, CoreApi)
