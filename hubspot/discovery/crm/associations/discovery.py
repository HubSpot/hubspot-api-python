import hubspot.crm.associations as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def types_api(self) -> api_client.TypesApi:
        return self._configure_api_client(api_client, "TypesApi")
