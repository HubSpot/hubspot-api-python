from ..discovery_base import DiscoveryBase
from .audit_logs.discovery import Discovery as AuditLogsDiscovery
from .blogs.discovery import Discovery as BlogsDiscovery
from .domains.discovery import Discovery as DomainsDiscovery
from .hubdb.discovery import Discovery as HubdbDiscovery
from .performance.discovery import Discovery as PerformanceDiscovery
from .site_search.discovery import Discovery as SiteSearchDiscovery
from .url_redirects.discovery import Discovery as UrlRedirectsDiscovery


class Discovery(DiscoveryBase):
    @property
    def audit_logs(self):
        return AuditLogsDiscovery(self.config)

    @property
    def blogs(self):
        return BlogsDiscovery(self.config)

    @property
    def domains(self):
        return DomainsDiscovery(self.config)

    @property
    def hubdb(self):
        return HubdbDiscovery(self.config)

    @property
    def performance(self):
        return PerformanceDiscovery(self.config)

    @property
    def site_search(self):
        return SiteSearchDiscovery(self.config)

    @property
    def url_redirects(self):
        return UrlRedirectsDiscovery(self.config)
