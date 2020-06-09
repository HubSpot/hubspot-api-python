import hubspot
from hubspot.cms.audit_logs import DefaultApi


def test_is_discoverable():
    apis = hubspot.Client.create().cms.audit_logs
    assert isinstance(apis.default_api, DefaultApi)
