import hubspot.cms.performance as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def public_performance_api(self) -> api_client.PublicPerformanceApi:
        return self._configure_api_client(api_client, "PublicPerformanceApi")
