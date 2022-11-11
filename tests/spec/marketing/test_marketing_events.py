from hubspot import HubSpot
from hubspot.marketing.events import AttendanceSubscriberStateChangesApi, MarketingEventsExternalApi, SettingsExternalApi


def test_is_discoverable():
    apis = HubSpot().marketing.events 
    assert isinstance(apis.attendance_subscriber_state_changes_api, AttendanceSubscriberStateChangesApi)
    assert isinstance(apis.marketing_events_external_api, MarketingEventsExternalApi)
    assert isinstance(apis.settings_external_api, SettingsExternalApi)
