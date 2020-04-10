from ...discovery_base import DiscoveryBase
from .cards.discovery import Discovery as CardsDiscovery


class Discovery(DiscoveryBase):
    def cards(self):
        return CardsDiscovery(self.config)

