from flask import Blueprint, render_template, request, redirect, url_for, session
from helpers.hubspot import create_client
from helpers.session import SessionKey
from auth import auth_required
from hubspot.crm.properties import PropertyUpdate, PropertyCreate
from hubspot.crm import ObjectType

module = Blueprint('properties', __name__)


@module.route('/')
@auth_required
def list():
    hubspot = create_client()
    properties = hubspot.crm.properties.core_api.get_all(ObjectType.CONTACTS)

    return render_template(
        'properties/list.html',
        properties=properties.results,
        action_performed=session.pop(SessionKey.ACTION_PERFORMED, None),
    )


@module.route('/new')
@auth_required
def new():
    property_create = PropertyCreate(
        type='string',
        group_name='contactinformation',
    )

    return render_template(
        'properties/show.html',
        property=property_create,
    )


@module.route('/new', methods=['POST'])
@auth_required
def create():
    property_create = PropertyCreate(**request.form)
    hubspot = create_client()
    property = hubspot.crm.properties.core_api.create(
        ObjectType.CONTACTS,
        property_create=property_create
    )
    session[SessionKey.ACTION_PERFORMED] = 'created'
    return redirect(
        url_for('properties.show', name=property.name),
        code=302
    )


@module.route('/<name>')
@auth_required
def show(name):
    hubspot = create_client()
    property = hubspot.crm.properties.core_api.get_by_name(ObjectType.CONTACTS, name)

    return render_template(
        'properties/show.html',
        property=property,
        action_performed=session.pop(SessionKey.ACTION_PERFORMED, None),
    )


@module.route('/<name>', methods=['POST'])
@auth_required
def update(name):
    property_update = PropertyUpdate(**request.form)
    hubspot = create_client()
    hubspot.crm.properties.core_api.update(ObjectType.CONTACTS, name, property_update=property_update)
    session[SessionKey.ACTION_PERFORMED] = 'updated'
    return redirect(request.url, code=302)


@module.route('/delete/<name>')
@auth_required
def delete(name):
    hubspot = create_client()
    hubspot.crm.properties.core_api.archive(ObjectType.CONTACTS, name)
    session[SessionKey.ACTION_PERFORMED] = 'deleted'
    return redirect(url_for('properties.list'), code=302)
