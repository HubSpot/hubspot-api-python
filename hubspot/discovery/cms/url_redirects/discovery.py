import hubspot.cms.url_redirects as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def redirects_api(self) -> api_client.RedirectsApi:
        return self._configure_api_client(api_client, "RedirectsApi")
