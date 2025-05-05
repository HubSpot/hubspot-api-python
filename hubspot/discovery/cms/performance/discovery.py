import warnings
import hubspot.cms.performance as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def public_performance_api(self) -> api_client.PublicPerformanceApi:
        warnings.warn(
        "cms.public_performance_api() is deprecated and will be removed in a future version.",
        DeprecationWarning,
        stacklevel=2
        )
        return self._configure_api_client(api_client, "PublicPerformanceApi")
