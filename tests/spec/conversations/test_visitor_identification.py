from hubspot import HubSpot
from hubspot.conversations.visitor_identification import GenerateApi


def test_is_discoverable():
    apis = HubSpot().conversations.visitor_identification
    assert isinstance(apis.generate_api, GenerateApi)
