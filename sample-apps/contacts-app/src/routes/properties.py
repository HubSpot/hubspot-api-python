from flask import Blueprint, render_template, request, redirect
from pprint import pprint
from helpers.hubspot import create_client
from auth import auth_required
from hubspot.crm.properties import PropertyUpdate

module = Blueprint(__name__, __name__)


@module.route('/')
@auth_required
def list():
    hubspot = create_client()
    properties = hubspot.crm().properties().core_api().get_all('CONTACTS')

    return render_template('properties/list.html', properties=properties.results)


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
    pprint(request.form)
    pprint(name)
    property_update = PropertyUpdate(**request.form)
    hubspot = create_client()
    hubspot.crm().properties().core_api().update('CONTACTS', name, property_update=property_update)
    return redirect(request.url, code=302)
