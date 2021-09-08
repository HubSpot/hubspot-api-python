from hubspot import HubSpot
from hubspot.cms.audit_logs import AuditLogsApi


def test_is_discoverable():
    apis = HubSpot().cms.audit_logs
    assert isinstance(apis.audit_logs_api, AuditLogsApi)
