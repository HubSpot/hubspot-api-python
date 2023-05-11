import hubspot.crm.associations.v4.schema as api_client
from .....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):

    @property
    def definitions_api(self) -> api_client.DefinitionsApi:
        return self._configure_api_client(api_client, "DefinitionsApi")

