import hubspot.conversations.visitor_identification as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def generate_api(self) -> api_client.GenerateApi:
        return self._configure_api_client(api_client, "GenerateApi")
