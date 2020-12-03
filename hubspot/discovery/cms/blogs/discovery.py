from ...discovery_base import DiscoveryBase
from .authors.discovery import Discovery as AuthorsDiscovery
from .blog_posts.discovery import Discovery as BlogPostsDiscovery
from .tags.discovery import Discovery as TagsDiscovery


class Discovery(DiscoveryBase):
    @property
    def authors(self):
        return AuthorsDiscovery(self.config)

    @property
    def blog_posts(self):
        return BlogPostsDiscovery(self.config)

    @property
    def tags(self):
        return TagsDiscovery(self.config)
