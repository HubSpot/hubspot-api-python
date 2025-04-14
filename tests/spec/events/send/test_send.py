from hubspot import HubSpot
from hubspot.events.send import BasicApi, BatchApi


def test_is_discoverable():
    apis = HubSpot().events.send
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
