from hubspot import HubSpot
from hubspot.events import EventsApi


def test_is_discoverable():
    apis = HubSpot().events
    assert isinstance(apis.events_api, EventsApi)
