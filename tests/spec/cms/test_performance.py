import hubspot
from hubspot.cms.performance import DefaultApi


def test_is_discoverable():
    apis = hubspot.Client.create().cms.performance
    assert isinstance(apis.default_api, DefaultApi)
