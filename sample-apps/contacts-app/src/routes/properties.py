from flask import Blueprint, render_template, request, redirect, url_for
from helpers.hubspot import create_client
from auth import auth_required
from hubspot.crm.properties import PropertyUpdate, PropertyCreate

module = Blueprint(__name__, __name__)


@module.route('/')
@auth_required
def list():
    hubspot = create_client()
    properties = hubspot.crm().properties().core_api().get_all('CONTACTS')

    return render_template('properties/list.html', properties=properties.results)


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
    property = hubspot.crm().properties().core_api().create(
        'CONTACTS',
        property_create=property_create
    )
    return redirect(
        url_for('routes.properties.show', name=property.name),
        code=302
    )


@module.route('/<name>')
@auth_required
def show(name):
    hubspot = create_client()
    property = hubspot.crm().properties().core_api().get_by_name('CONTACTS', name)

    return render_template(
        'properties/show.html',
        property=property,
    )


@module.route('/<name>', methods=['POST'])
@auth_required
def update(name):
    property_update = PropertyUpdate(**request.form)
    hubspot = create_client()
    hubspot.crm().properties().core_api().update('CONTACTS', name, property_update=property_update)
    return redirect(request.url, code=302)