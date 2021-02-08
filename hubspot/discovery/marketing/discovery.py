from ..discovery_base import DiscoveryBase
from .transactional.discovery import Discovery as TransactionalDiscovery


class Discovery(DiscoveryBase):
    @property
    def transactional(self):
        return TransactionalDiscovery(self.config)
