import datetime
from flask import Blueprint, render_template, request, jsonify
from auth import auth_required
from services.db import session, Event
from helpers.hubspot import create_client
from hubspot.crm.contacts import BatchReadInputSimplePublicObjectId, SimplePublicObjectId

module = Blueprint("events", __name__)


@module.route("/")
@auth_required
def list():
    events = session.query(Event).order_by(Event.occurred_at.desc()).limit(50).all()
    session.commit()
    hubspot = create_client()

    inputs = [SimplePublicObjectId(id=e.object_id) for e in events]
    batch_read_input_simple_public_object_id = BatchReadInputSimplePublicObjectId(
        inputs=inputs,
    )
    contacts = hubspot.crm.contacts.batch_api.read(
        batch_read_input_simple_public_object_id=batch_read_input_simple_public_object_id,
    ).results
    contacts_dict = {int(contact.id): contact for contact in contacts}

    return render_template(
        "events/list.html",
        events=events,
        contacts_dict=contacts_dict,
        now=datetime.datetime.now()
    )


@module.route("/updates")
def updates():
    after = datetime.datetime.fromisoformat(request.args.get('after'))
    updates_count = session.query(Event).filter(Event.created_at > after).count()
    session.commit()

    return jsonify({
        "updatesCount": updates_count,
    })
