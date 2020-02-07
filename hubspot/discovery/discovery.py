from .auth.discovery import Discovery as AuthDiscovery
from .discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    def auth(self):
        return AuthDiscovery(self.config)
