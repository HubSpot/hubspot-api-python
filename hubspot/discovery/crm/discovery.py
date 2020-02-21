from ..discovery_base import DiscoveryBase
from .contacts.discovery import Discovery as ContactsDiscovery
from .companies.discovery import Discovery as CompaniesDiscovery


class Discovery(DiscoveryBase):
    def contacts(self):
        return ContactsDiscovery(self.config)

    def companies(self):
        return CompaniesDiscovery(self.config)
