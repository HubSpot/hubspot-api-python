from ..discovery_base import DiscoveryBase

class Discovery(DiscoveryBase):
    @property
    def audit_logs(self):
        from .audit_logs.discovery import Discovery as AuditLogsDiscovery
        return AuditLogsDiscovery(self.config)

    @property
    def blogs(self):
        from .blogs.discovery import Discovery as BlogsDiscovery
        return BlogsDiscovery(self.config)

    @property
    def domains(self):
        from .domains.discovery import Discovery as DomainsDiscovery
        return DomainsDiscovery(self.config)

    @property
    def hubdb(self):
        from .hubdb.discovery import Discovery as HubdbDiscovery
        return HubdbDiscovery(self.config)

    @property
    def performance(self):
        from .performance.discovery import Discovery as PerformanceDiscovery
        return PerformanceDiscovery(self.config)

    @property
    def site_search(self):
        from .site_search.discovery import Discovery as SiteSearchDiscovery
        return SiteSearchDiscovery(self.config)

    @property
    def source_code(self):
        from .source_code.discovery import Discovery as SourceCodeDiscovery
        return SourceCodeDiscovery(self.config)

    @property
    def url_redirects(self):
        from .url_redirects.discovery import Discovery as UrlRedirectsDiscovery
        return UrlRedirectsDiscovery(self.config)
