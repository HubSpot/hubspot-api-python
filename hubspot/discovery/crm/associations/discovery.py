import hubspot.crm.associations as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def v4(self):
        from .v4.discovery import Discovery as v4Discovery
        return v4Discovery(self.config)

    @property
    def schema(self):
        from .schema.discovery import Discovery as schemaDiscovery
        return schemaDiscovery(self.config)

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

