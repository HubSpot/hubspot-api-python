import hubspot.auth.oauth as oauth
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    def default_api(self) -> oauth.DefaultApi:
        return self._configure_api_client(oauth, 'DefaultApi')
