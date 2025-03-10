import hubspot.crm.contacts as api_client
from hubspot.utils.objects import fetch_all
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def gdpr_api(self) -> api_client.GDPRApi:
        return self._configure_api_client(api_client, "GDPRApi")

    @property
    def merge_api(self) -> api_client.MergeApi:
        return self._configure_api_client(api_client, "MergeApi")

    @property
    def search_api(self) -> api_client.SearchApi:
        return self._configure_api_client(api_client, "SearchApi")

    def get_all(self, **kwargs):
        return fetch_all(self.basic_api, **kwargs)
