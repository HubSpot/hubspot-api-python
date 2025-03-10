import hubspot.crm.lists as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def folders_api(self) -> api_client.FoldersApi:
        return self._configure_api_client(api_client, "FoldersApi")

    @property
    def lists_api(self) -> api_client.ListsApi:
        return self._configure_api_client(api_client, "ListsApi")

    @property
    def mapping_api(self) -> api_client.MappingApi:
        return self._configure_api_client(api_client, "MappingApi")

    @property
    def memberships_api(self) -> api_client.MembershipsApi:
        return self._configure_api_client(api_client, "MembershipsApi")
