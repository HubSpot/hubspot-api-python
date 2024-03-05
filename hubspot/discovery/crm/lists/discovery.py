import hubspot.crm.lists as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def list_app_api(self) -> api_client.ListAppApi:
        return self._configure_api_client(api_client, "ListAppApi")

    @property
    def list_app_membership_api(self) -> api_client.ListAppMembershipApi:
        return self._configure_api_client(api_client, "ListAppMembershipApi")
