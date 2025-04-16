import hubspot.marketing.events as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def add_event_attendees_api(self) -> api_client.AddEventAttendeesApi:
        return self._configure_api_client(api_client, "AddEventAttendeesApi")

    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def change_property_api(self) -> api_client.ChangePropertyApi:
        return self._configure_api_client(api_client, "ChangePropertyApi")

    @property
    def identifiers_api(self) -> api_client.IdentifiersApi:
        return self._configure_api_client(api_client, "IdentifiersApi")

    @property
    def list_associations_api(self) -> api_client.ListAssociationsApi:
        return self._configure_api_client(api_client, "ListAssociationsApi")

    @property
    def retrieve_participant_state_api(self) -> api_client.RetrieveParticipantStateApi:
        return self._configure_api_client(api_client, "RetrieveParticipantStateApi")

    @property
    def settings_api(self) -> api_client.SettingsApi:
        return self._configure_api_client(api_client, "SettingsApi")

    @property
    def subscriber_state_changes_api(self) -> api_client.SubscriberStateChangesApi:
        return self._configure_api_client(api_client, "SubscriberStateChangesApi")
