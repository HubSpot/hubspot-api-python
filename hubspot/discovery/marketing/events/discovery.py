import hubspot.marketing.events as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def search_api(self) -> api_client.SearchApi:
        return self._configure_api_client(api_client, "SearchApi")

    @property
    def settings_api(self) -> api_client.SettingsApi:
        return self._configure_api_client(api_client, "SettingsApi")

    @property
    def subscriber_state_changes_api(self) -> api_client.SubscriberStateChangesApi:
        return self._configure_api_client(api_client, "SubscriberStateChangesApi")