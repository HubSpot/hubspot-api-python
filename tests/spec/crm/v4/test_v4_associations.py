from hubspot import HubSpot
from hubspot.crm.associations.v4 import BatchApi, BasicApi, ReportApi


def test_is_discoverable():
    apis = HubSpot().crm.associations.v4
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.report_api, ReportApi)
    assert hasattr(apis, "schema")
