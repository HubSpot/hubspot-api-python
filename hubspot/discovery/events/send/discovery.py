import hubspot.events.send as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def custom_event_data_api(self) -> api_client.CustomEventDataApi:
        return self._configure_api_client(api_client, "CustomEventDataApi")
