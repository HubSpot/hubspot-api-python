import hubspot.oauth.v3 as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def advanced_api(self) -> api_client.AdvancedApi:
        return self._configure_api_client(api_client, "AdvancedApi")
