from hubspot import HubSpot
from hubspot.marketing.events import (
    AttendanceSubscriberStateChangesApi,
    BasicApi,
    ParticipantStateApi,
    SettingsApi,
    SubscriberStateChangesApi
)


def test_is_discoverable():
    apis = HubSpot().marketing.events
    assert isinstance(apis.attendance_subscriber_state_changes_api, AttendanceSubscriberStateChangesApi)
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.participant_state_api, ParticipantStateApi)
    assert isinstance(apis.settings_api, SettingsApi)
    assert isinstance(apis.subscriber_state_changes_api, SubscriberStateChangesApi)
