import hubspot.cms.audit_logs as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def audit_logs_api(self) -> api_client.AuditLogsApi:
        return self._configure_api_client(api_client, "AuditLogsApi")
