from hubspot import HubSpot
from hubspot.automation.actions import (
    CallbacksApi,
    DefinitionsApi,
    FunctionsApi,
    RevisionsApi,
)


def test_is_discoverable():
    apis = HubSpot().automation.actions
    assert isinstance(apis.callbacks_api, CallbacksApi)
    assert isinstance(apis.definitions_api, DefinitionsApi)
    assert isinstance(apis.functions_api, FunctionsApi)
    assert isinstance(apis.revisions_api, RevisionsApi)
