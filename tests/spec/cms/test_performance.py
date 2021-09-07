from hubspot import HubSpot
from hubspot.cms.performance import PublicPerformanceApi


def test_is_discoverable():
    apis = HubSpot().cms.performance
    assert isinstance(apis.public_performance_api, PublicPerformanceApi)
