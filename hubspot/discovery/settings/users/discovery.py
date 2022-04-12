import hubspot.settings.users as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def roles_api(self) -> api_client.RolesApi:
        return self._configure_api_client(api_client, "RolesApi")

    @property
    def teams_api(self) -> api_client.TeamsApi:
        return self._configure_api_client(api_client, "TeamsApi")

    @property
    def users_api(self) -> api_client.UsersApi:
        return self._configure_api_client(api_client, "UsersApi")
