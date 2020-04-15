from .oauth.discovery import Discovery as OAuthDiscovery
from ..discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def oauth(self):
        return OAuthDiscovery(self.config)
