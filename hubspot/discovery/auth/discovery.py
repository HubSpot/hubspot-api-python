from ..discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def oauth(self):
        from .oauth.discovery import Discovery as OAuthDiscovery
        return OAuthDiscovery(self.config)
