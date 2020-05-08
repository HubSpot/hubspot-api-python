import hubspot
from hubspot.webhooks import SubscriptionsApi, SettingsApi


def test_is_discoverable():
    apis = hubspot.Client.create().webhooks
    assert isinstance(apis.settings_api, SettingsApi)
    assert isinstance(apis.subscriptions_api, SubscriptionsApi)
