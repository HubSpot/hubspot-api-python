import hubspot
from hubspot.cms.domains import DomainsApi


def test_is_discoverable():
    apis = hubspot.Client.create().cms.domains
    assert isinstance(apis.domains_api, DomainsApi)
