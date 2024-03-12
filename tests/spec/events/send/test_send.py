from hubspot import HubSpot
from hubspot.events.send import CustomEventDataApi


def test_is_discoverable():
    apis = HubSpot().events.send
    assert isinstance(apis.custom_event_data_api, CustomEventDataApi)
