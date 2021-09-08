import hubspot.crm.schemas as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def public_object_schemas_api(self) -> api_client.PublicObjectSchemasApi:
        return self._configure_api_client(api_client, "PublicObjectSchemasApi")

    @property
    def core_api(self) -> api_client.CoreApi:
        return self._configure_api_client(api_client, "CoreApi")
