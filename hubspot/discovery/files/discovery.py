from ..discovery_base import DiscoveryBase

class Discovery(DiscoveryBase):
    @property
    def files(self):
        from .files.discovery import Discovery as FilesDiscovery
        return FilesDiscovery(self.config)
