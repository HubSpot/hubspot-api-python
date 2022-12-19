from hubspot import HubSpot
from hubspot.crm.extensions.accounting import (
    CallbacksApi,
    InvoiceApi,
    SettingsApi,
    SyncApi,
    UserAccountsApi
)


def test_is_discoverable():
    apis = HubSpot().crm.extensions.accounting
    assert isinstance(apis.callbacks_api, CallbacksApi)
    assert isinstance(apis.invoice_api, InvoiceApi)
    assert isinstance(apis.settings_api, SettingsApi)
    assert isinstance(apis.sync_api, SyncApi)
    assert isinstance(apis.user_accounts_api, UserAccountsApi)
