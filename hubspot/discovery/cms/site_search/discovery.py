import hubspot.cms.site_search as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def public_api(self) -> api_client.PublicApi:
        return self._configure_api_client(api_client, "PublicApi")
