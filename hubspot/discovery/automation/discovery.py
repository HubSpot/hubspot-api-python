from ..discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def actions(self):
        from .actions.discovery import Discovery as ActionsDiscovery
        return ActionsDiscovery(self.config)
