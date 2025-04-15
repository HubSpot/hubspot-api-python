from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def invoices(self):
        from .invoices.discovery import Discovery as InvoicesDiscovery
        return InvoicesDiscovery(self.config)
