import hubspot.crm.exports as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def public_exports_api(self) -> api_client.PublicExportsApi:
        return self._configure_api_client(api_client, "PublicExportsApi")
