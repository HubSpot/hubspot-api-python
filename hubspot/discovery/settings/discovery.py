from ..discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def users(self):
        from .users.discovery import Discovery as UsersDiscovery
        return UsersDiscovery(self.config)
