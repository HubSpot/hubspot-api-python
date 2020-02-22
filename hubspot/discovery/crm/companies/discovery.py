import hubspot.codegen.crm.companies as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, 'BasicApi')

    def associations_api(self) -> api_client.AssociationsApi:
        return self._configure_api_client(api_client, 'AssociationsApi')

    def search_api(self) -> api_client.SearchApi:
        return self._configure_api_client(api_client, 'SearchApi')

    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, 'BatchApi')

    def exceptions(self):
        return api_client.exceptions
