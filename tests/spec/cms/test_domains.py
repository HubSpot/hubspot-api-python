from hubspot import HubSpot
from hubspot.cms.domains import DomainsApi


def test_is_discoverable():
    apis = HubSpot().cms.domains
    assert isinstance(apis.domains_api, DomainsApi)
