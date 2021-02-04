import hubspot.crm.extensions.accounting as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def callbacks_api(self) -> api_client.CallbacksApi:
        return self._configure_api_client(api_client, "CallbacksApi")

    @property
    def invoice_api(self) -> api_client.InvoiceApi:
        return self._configure_api_client(api_client, "InvoiceApi")

    @property
    def settings_api(self) -> api_client.SettingsApi:
        return self._configure_api_client(api_client, "SettingsApi")

    @property
    def sync_api(self) -> api_client.SyncApi:
        return self._configure_api_client(api_client, "SyncApi")

    @property
    def user_accounts_api(self) -> api_client.UserAccountsApi:
        return self._configure_api_client(api_client, "UserAccountsApi")
