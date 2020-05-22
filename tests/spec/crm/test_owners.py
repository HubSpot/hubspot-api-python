import hubspot
from hubspot.crm.owners import DefaultApi


def test_is_discoverable():
    apis = hubspot.Client.create().crm.owners
    assert isinstance(apis.default_api, DefaultApi)
    assert hasattr(apis, "get_all")
