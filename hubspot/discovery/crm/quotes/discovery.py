import hubspot.crm.quotes as api_client
from hubspot.utils.objects import fetch_all
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def associations_api(self) -> api_client.AssociationsApi:
        return self._configure_api_client(api_client, "AssociationsApi")

    @property
    def search_api(self) -> api_client.SearchApi:
        return self._configure_api_client(api_client, "SearchApi")

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    def get_all(self, **kwargs):
        return fetch_all(self.basic_api, **kwargs)
