from hubspot import HubSpot
from hubspot.crm.associations.v4.schema import DefinitionsApi, DefinitionConfigurationsApi


def test_is_discoverable():
    apis = HubSpot().crm.associations.v4.schema
    assert isinstance(apis.definitions_api, DefinitionsApi)
    assert isinstance(apis.definition_configurations_api, DefinitionConfigurationsApi)
