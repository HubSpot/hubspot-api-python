import hubspot.crm.objects.emails as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def search_api(self) -> api_client.SearchApi:
        return self._configure_api_client(api_client, "SearchApi")

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def public_object_api(self) -> api_client.PublicObjectApi:
        return self._configure_api_client(api_client, "PublicObjectApi")
