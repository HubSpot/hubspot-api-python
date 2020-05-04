import hubspot.crm.properties as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def core_api(self) -> api_client.CoreApi:
        return self._configure_api_client(api_client, "CoreApi")

    @property
    def groups_api(self) -> api_client.GroupsApi:
        return self._configure_api_client(api_client, "GroupsApi")
