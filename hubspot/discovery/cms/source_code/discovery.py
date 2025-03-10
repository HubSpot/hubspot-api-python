import hubspot.cms.source_code as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def content_api(self) -> api_client.ContentApi:
        return self._configure_api_client(api_client, "ContentApi")

    @property
    def extract_api(self) -> api_client.ExtractApi:
        return self._configure_api_client(api_client, "ExtractApi")

    @property
    def metadata_api(self) -> api_client.MetadataApi:
        return self._configure_api_client(api_client, "MetadataApi")

    @property
    def validation_api(self) -> api_client.ValidationApi:
        return self._configure_api_client(api_client, "ValidationApi")
