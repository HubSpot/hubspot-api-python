from hubspot import HubSpot
from hubspot.discovery.automation.actions.discovery import Discovery


def test_is_discoverable():
    apis = HubSpot().automation
    assert isinstance(apis.actions, Discovery)
