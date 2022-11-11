import hubspot.marketing.events as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def attendance_subscriber_state_changes_api(self) -> api_client.AttendanceSubscriberStateChangesApi:
        return self._configure_api_client(api_client, "AttendanceSubscriberStateChangesApi")

    @property
    def marketing_events_external_api(self) -> api_client.MarketingEventsExternalApi:
        return self._configure_api_client(api_client, "MarketingEventsExternalApi")

    @property
    def settings_external_api(self) -> api_client.SettingsExternalApi:
        return self._configure_api_client(api_client, "SettingsExternalApi")
