from ..discovery_base import DiscoveryBase
from .visitor_identification.discovery import Discovery as VisitorIdentificationDiscovery


class Discovery(DiscoveryBase):
    @property
    def visitor_identification(self):
        return VisitorIdentificationDiscovery(self.config)
