import hubspot.cms.blogs.authors as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def author_api(self) -> api_client.BlogAuthorsApi:
        return self._configure_api_client(api_client, "BlogAuthorsApi")
