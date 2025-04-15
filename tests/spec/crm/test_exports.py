from hubspot import HubSpot
from hubspot.crm.exports import PublicExportsApi


def test_is_discoverable():
    apis = HubSpot().crm.exports
    assert isinstance(apis.public_exports_api, PublicExportsApi)
