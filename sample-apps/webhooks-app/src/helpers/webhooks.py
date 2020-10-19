import json
from hubspot import Client
from hubspot.webhooks import (
    SubscriptionCreateRequest,
    BatchInputSubscriptionBatchUpdateRequest,
    SubscriptionPatchRequest,
    SettingsChangeRequest,
    ApiException,
    SubscriptionBatchUpdateRequest,
)


def pause_active_subscriptions(hubspot_client: Client, app_id: str):
    subscriptions = hubspot_client.webhooks.subscriptions_api.get_all(app_id=app_id)
    active_subscriptions = [s for s in subscriptions.results if s.active]

    if len(active_subscriptions) > 0:
        inputs = [
            SubscriptionBatchUpdateRequest(id=s.id, active=False)
            for s in active_subscriptions
        ]
        batch_input_subscription_batch_update_request = (
            BatchInputSubscriptionBatchUpdateRequest(
                inputs=inputs,
            )
        )
        hubspot_client.webhooks.subscriptions_api.update_batch(
            app_id=app_id,
            batch_input_subscription_batch_update_request=batch_input_subscription_batch_update_request,
        )


def configure_target_url(hubspot_client: Client, app_id: str, target_url: str):
    settings_change_request = SettingsChangeRequest(target_url=target_url)
    hubspot_client.webhooks.settings_api.configure(
        app_id=app_id,
        settings_change_request=settings_change_request,
    )


def create_or_activate_subscription(
    hubspot_client: Client, app_id: str, event_type: str, property_name=None
):
    try:
        subscription_create_request = SubscriptionCreateRequest(
            active=True,
            event_type=event_type,
            property_name=property_name,
        )
        hubspot_client.webhooks.subscriptions_api.create(
            app_id=app_id,
            subscription_create_request=subscription_create_request,
        )
    except ApiException as e:
        existing_subscription_id = json.loads(
            json.loads(e.body)["context"]["subscriptionIds"][0]
        )[0]
        subscription_patch_request = SubscriptionPatchRequest(enabled=True)
        hubspot_client.webhooks.subscriptions_api.update(
            subscription_id=existing_subscription_id,
            app_id=app_id,
            subscription_patch_request=subscription_patch_request,
        )
