from ...discovery_base import DiscoveryBase

class Discovery(DiscoveryBase):
    @property
    def authors(self):
        from .authors.discovery import Discovery as AuthorsDiscovery
        return AuthorsDiscovery(self.config)

    @property
    def blog_posts(self):
        from .blog_posts.discovery import Discovery as BlogPostsDiscovery
        return BlogPostsDiscovery(self.config)

    @property
    def tags(self):
        from .tags.discovery import Discovery as TagsDiscovery
        return TagsDiscovery(self.config)
