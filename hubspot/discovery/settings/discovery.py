from ..discovery_base import DiscoveryBase
from .users.discovery import Discovery as UsersDiscovery


class Discovery(DiscoveryBase):
    @property
    def users(self):
        return UsersDiscovery(self.config)
