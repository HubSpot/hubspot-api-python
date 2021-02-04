from ...discovery_base import DiscoveryBase
from .cards.discovery import Discovery as CardsDiscovery
from .accounting.discovery import Discovery as AccountingDiscovery
from .calling.discovery import Discovery as CallingDiscovery
from .videoconferencing.discovery import Discovery as VideoconferencingDiscovery

class Discovery(DiscoveryBase):
    @property
    def cards(self):
        return CardsDiscovery(self.config)

    @property
    def accounting(self):
        return AccountingDiscovery(self.config)

    @property
    def calling(self):
        return CallingDiscovery(self.config)

    @property
    def videoconferencing(self):
        return VideoconferencingDiscovery(self.config)
