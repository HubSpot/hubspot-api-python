import hubspot.crm.extensions.cards as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    def exceptions(self):
        return api_client.exceptions
