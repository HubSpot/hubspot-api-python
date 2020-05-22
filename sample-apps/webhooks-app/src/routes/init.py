import os
from flask import Blueprint, render_template, redirect, url_for, request
from auth import auth_required
from helpers.hubspot import create_client_with_developer_api_key
from helpers.webhooks import (
    create_or_activate_subscription,
    configure_target_url,
    pause_active_subscriptions,
)

module = Blueprint("init", __name__)


@module.route("/")
@auth_required
def readme():
    target_url = url_for("webhooks.handle", _external=True)
    return render_template("init/readme.html", target_url=target_url)


@module.route("/", methods=["POST"])
@auth_required
def start():
    hubspot = create_client_with_developer_api_key()
    app_id = os.getenv("HUBSPOT_APPLICATION_ID")

    pause_active_subscriptions(hubspot_client=hubspot, app_id=app_id)

    target_url = url_for("webhooks.handle", _external=True)
    configure_target_url(hubspot_client=hubspot, app_id=app_id, target_url=target_url)

    subscriptions = [
        {"event_type": "contact.propertyChange", "property_name": "firstname"},
        {"event_type": "contact.creation"},
        {"event_type": "contact.deletion"},
    ]
    for subscription in subscriptions:
        create_or_activate_subscription(
            hubspot_client=hubspot, app_id=app_id, **subscription
        )

    return redirect(url_for("events.list"))
