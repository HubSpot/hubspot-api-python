from ..discovery_base import DiscoveryBase
from .actions.discovery import Discovery as ActionsDiscovery


class Discovery(DiscoveryBase):
    @property
    def actions(self):
        return ActionsDiscovery(self.config)
