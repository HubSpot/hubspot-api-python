from .discovery_base import DiscoveryBase
from .auth.discovery import Discovery as AuthDiscovery
from .crm.discovery import Discovery as CrmDiscovery


class Discovery(DiscoveryBase):
    def auth(self):
        return AuthDiscovery(self.config)

    def crm(self):
        return CrmDiscovery(self.config)
