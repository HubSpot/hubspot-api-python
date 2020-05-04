from ...discovery_base import DiscoveryBase
from .cards.discovery import Discovery as CardsDiscovery


class Discovery(DiscoveryBase):
    @property
    def cards(self):
        return CardsDiscovery(self.config)
