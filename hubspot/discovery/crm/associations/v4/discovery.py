import hubspot.crm.associations.v4 as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def report_api(self) -> api_client.ReportApi:
        return self._configure_api_client(api_client, "ReportApi")

    @property
    def schema(self):
        from .schema.discovery import Discovery as schemaDiscovery
        return schemaDiscovery(self.config)
