import hubspot.crm.imports as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    def core_api(self) -> api_client.CoreApi:
        return self._configure_api_client(api_client, 'CoreApi')
