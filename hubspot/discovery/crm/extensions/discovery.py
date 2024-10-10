from ...discovery_base import DiscoveryBase

class Discovery(DiscoveryBase):
    @property
    def cards(self):
        from .cards.discovery import Discovery as CardsDiscovery
        return CardsDiscovery(self.config)

    @property
    def calling(self):
        from .calling.discovery import Discovery as CallingDiscovery
        return CallingDiscovery(self.config)

    @property
    def videoconferencing(self):
        from .videoconferencing.discovery import Discovery as VideoconferencingDiscovery
        return VideoconferencingDiscovery(self.config)
