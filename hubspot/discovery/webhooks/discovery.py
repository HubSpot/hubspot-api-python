import hubspot.webhooks as api_client
from ..discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def settings_api(self) -> api_client.SettingsApi:
        return self._configure_api_client(api_client, "SettingsApi")

    @property
    def subscriptions_api(self) -> api_client.SubscriptionsApi:
        return self._configure_api_client(api_client, "SubscriptionsApi")
