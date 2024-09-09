from hubspot import HubSpot
from hubspot.events import DefaultApi, EventsApi


def test_is_discoverable():
    apis = HubSpot().events
    assert isinstance(apis.default_api, DefaultApi)
    assert isinstance(apis.events_api, EventsApi)
