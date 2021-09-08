import hubspot.crm.owners as api_client
from hubspot.utils.objects import fetch_all
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def owners_api(self) -> api_client.OwnersApi:
        return self._configure_api_client(api_client, "OwnersApi")

    def get_all(self, **kwargs):
        return fetch_all(self.owners_api, **kwargs)
