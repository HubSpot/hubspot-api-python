from hubspot import HubSpot
from hubspot.communication_preferences import DefinitionApi, StatusApi


def test_is_discoverable():
    apis = HubSpot().communication_preferences
    assert isinstance(apis.definition_api, DefinitionApi)
    assert isinstance(apis.status_api, StatusApi)
