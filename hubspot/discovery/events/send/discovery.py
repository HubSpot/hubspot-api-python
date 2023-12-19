import hubspot.events.send as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def behavioral_events_tracking_api(self) -> api_client.BehavioralEventsTrackingApi:
        return self._configure_api_client(api_client, "BehavioralEventsTrackingApi")
