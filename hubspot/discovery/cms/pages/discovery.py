import hubspot.cms.pages as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def landing_pages_api(self) -> api_client.LandingPagesApi:
        return self._configure_api_client(api_client, "LandingPagesApi")

    @property
    def site_pages_api(self) -> api_client.SitePagesApi:
        return self._configure_api_client(api_client, "SitePagesApi")
