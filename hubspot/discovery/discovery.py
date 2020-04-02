from .discovery_base import DiscoveryBase
from .auth.discovery import Discovery as AuthDiscovery
from .crm.discovery import Discovery as CrmDiscovery
from .webhooks.discovery import Discovery as WebhooksDiscovery


class Discovery(DiscoveryBase):
    def auth(self):
        return AuthDiscovery(self.config)

    def crm(self):
        return CrmDiscovery(self.config)

    def webhooks(self):
        return WebhooksDiscovery(self.config)
