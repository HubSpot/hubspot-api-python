import hubspot.communication_preferences as api_client
from ..discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def definition_api(self) -> api_client.DefinitionApi:
        return self._configure_api_client(api_client, "DefinitionApi")

    @property
    def status_api(self) -> api_client.StatusApi:
        return self._configure_api_client(api_client, "StatusApi")
