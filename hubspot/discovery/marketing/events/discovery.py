import hubspot.marketing.events as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def attendance_subscriber_state_changes_api(self) -> api_client.AttendanceSubscriberStateChangesApi:
        return self._configure_api_client(api_client, "AttendanceSubscriberStateChangesApi")

    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def list_associations_api(self) -> api_client.ListAssociationsApi:
        return self._configure_api_client(api_client, "ListAssociationsApi")

    @property
    def participant_state_api(self) -> api_client.ParticipantStateApi:
        return self._configure_api_client(api_client, "ParticipantStateApi")

    @property
    def settings_api(self) -> api_client.SettingsApi:
        return self._configure_api_client(api_client, "SettingsApi")

    @property
    def subscriber_state_changes_api(self) -> api_client.SubscriberStateChangesApi:
        return self._configure_api_client(api_client, "SubscriberStateChangesApi")
