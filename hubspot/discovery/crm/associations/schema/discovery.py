import hubspot.crm.associations.schema as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):

    @property
    def types_api(self) -> api_client.TypesApi:
        return self._configure_api_client(api_client, "TypesApi")

