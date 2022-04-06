import hubspot.cms.blogs.tags as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def tag_api(self) -> api_client.BlogTagsApi:
        return self._configure_api_client(api_client, "BlogTagsApi")
