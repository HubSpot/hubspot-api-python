from hubspot import HubSpot
from hubspot.marketing.events import BasicApi, BatchApi, SearchApi, SettingsApi, SubscriberStateChangesApi


def test_is_discoverable():
    apis = HubSpot().marketing.events 
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)
    assert isinstance(apis.settings_api, SettingsApi)
    assert isinstance(apis.subscriber_state_changes_api, SubscriberStateChangesApi)
