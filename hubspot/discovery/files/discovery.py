from ..discovery_base import DiscoveryBase
from .files.discovery import Discovery as FilesDiscovery


class Discovery(DiscoveryBase):
    @property
    def files(self):
        return FilesDiscovery(self.config)
