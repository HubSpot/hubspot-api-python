import hubspot.marketing.transactional as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def default_api(self) -> api_client.DefaultApi:
        return self._configure_api_client(api_client, "DefaultApi")
