import hubspot.cms.hubdb as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def rows_api(self) -> api_client.RowsApi:
        return self._configure_api_client(api_client, "RowsApi")

    @property
    def rows_batch_api(self) -> api_client.RowsBatchApi:
        return self._configure_api_client(api_client, "RowsBatchApi")

    @property
    def tables_api(self) -> api_client.TablesApi:
        return self._configure_api_client(api_client, "TablesApi")
