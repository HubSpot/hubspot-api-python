from ..discovery_base import DiscoveryBase
from .contacts.discovery import Discovery as ContactsDiscovery


class Discovery(DiscoveryBase):
    def contacts(self):
        return ContactsDiscovery(self.config)
