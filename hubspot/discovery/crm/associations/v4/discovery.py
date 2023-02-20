import hubspot.crm.associations.v4 as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def definitions_api(self) -> api_client.DefinitionsApi:
        return self._configure_api_client(api_client, "DefinitionsApi")
