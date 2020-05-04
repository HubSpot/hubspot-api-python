import hubspot.crm.owners as api_client
from hubspot.utils.objects import fetch_all
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def default_api(self) -> api_client.DefaultApi:
        return self._configure_api_client(api_client, "DefaultApi")

    def get_all(self, **kwargs):
        return fetch_all(self.default_api, **kwargs)
