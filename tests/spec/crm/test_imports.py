from hubspot import HubSpot
from hubspot.crm.imports import CoreApi, PublicImportsApi


def test_is_discoverable():
    apis = HubSpot().crm.imports
    assert isinstance(apis.core_api, CoreApi)
    assert isinstance(apis.public_imports_api, PublicImportsApi)
