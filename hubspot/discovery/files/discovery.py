import hubspot.files as api_client
from ..discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def files_api(self) -> api_client.FilesApi:
        return self._configure_api_client(api_client, "FilesApi")

    @property
    def folders_api(self) -> api_client.FoldersApi:
        return self._configure_api_client(api_client, "FoldersApi")
