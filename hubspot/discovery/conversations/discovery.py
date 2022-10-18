from ..discovery_base import DiscoveryBase

class Discovery(DiscoveryBase):
    @property
    def visitor_identification(self):
        from .visitor_identification.discovery import Discovery as VisitorIdentificationDiscovery
        return VisitorIdentificationDiscovery(self.config)
