from hubspot import HubSpot
from hubspot.events.send import BehavioralEventsTrackingApi


def test_is_discoverable():
    apis = HubSpot().events.send
    assert isinstance(apis.behavioral_events_tracking_api, BehavioralEventsTrackingApi)
