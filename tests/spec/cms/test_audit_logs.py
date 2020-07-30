from hubspot import HubSpot
from hubspot.cms.audit_logs import DefaultApi


def test_is_discoverable():
    apis = HubSpot().cms.audit_logs
    assert isinstance(apis.default_api, DefaultApi)
