import hubspot.cms.blogs.blog_posts as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def blog_post_api(self) -> api_client.BlogPostsApi:
        return self._configure_api_client(api_client, "BlogPostsApi")
