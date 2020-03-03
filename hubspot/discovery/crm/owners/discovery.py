import hubspot.crm.owners as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):

    def default_api(self) -> api_client.DefaultApi:
        return self._configure_api_client(api_client, 'DefaultApi')

    def exceptions(self):
        return api_client.exceptions
