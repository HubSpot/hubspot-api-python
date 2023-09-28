import os

from hubspot.webhooks import SettingsChangeRequest


APP_ID = os.getenv("HUBSPOT_APP_ID")


def test_webhooks__get_all(api_client_by_api_key):
    result = api_client_by_api_key.webhooks.settings_api.get_all(app_id=APP_ID)

    assert result


def test_webhooks__configure(api_client_by_api_key):
    throttling = {
        "maxConcurrentRequests": 10,
        "period": "SECONDLY"
    }
    settings_change_request = SettingsChangeRequest(
        target_url="https://www.test.com/test/target",
        throttling=throttling
    )

    result = api_client_by_api_key.webhooks.settings_api.configure(
        app_id=APP_ID,
        settings_change_request=settings_change_request
    )

    assert result


def test_webhooks_subscriptions__get_all(api_client_by_api_key):
    result = api_client_by_api_key.webhooks.subscriptions_api.get_all(app_id=APP_ID)

    assert result
