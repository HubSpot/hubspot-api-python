from hubspot import HubSpot
from hubspot.marketing.events import (
    AddEventAttendeesApi,
    BasicApi,
    BatchApi,
    ChangePropertyApi,
    IdentifiersApi,
    ListAssociationsApi,
    RetrieveParticipantStateApi,
    SettingsApi,
    SubscriberStateChangesApi
)


def test_is_discoverable():
    apis = HubSpot().marketing.events
    assert isinstance(apis.add_event_attendees_api, AddEventAttendeesApi)
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.change_property_api, ChangePropertyApi)
    assert isinstance(apis.identifiers_api, IdentifiersApi)
    assert isinstance(apis.list_associations_api, ListAssociationsApi)
    assert isinstance(apis.retrieve_participant_state_api, RetrieveParticipantStateApi)
    assert isinstance(apis.settings_api, SettingsApi)
    assert isinstance(apis.subscriber_state_changes_api, SubscriberStateChangesApi)
