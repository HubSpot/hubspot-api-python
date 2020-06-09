import hubspot.cms.domains as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def domains_api(self) -> api_client.DomainsApi:
        return self._configure_api_client(api_client, "DomainsApi")
