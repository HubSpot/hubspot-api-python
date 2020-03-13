from flask import Blueprint, render_template, request, redirect
from helpers.hubspot import create_client
from auth import auth_required
from pprint import pprint
from hubspot.crm.contacts import PublicObjectSearchRequest, SimplePublicObject, Filter, FilterGroup

module = Blueprint(__name__, __name__)


@module.route('/')
@auth_required
def list():
    hubspot = create_client()
    contacts_page = hubspot.crm().contacts().basic_api().get_page()

    return render_template('contacts/list.html', contacts=contacts_page.results)


@module.route('/<contact_id>')
@auth_required
def show(contact_id):
    hubspot = create_client()
    all_properties = hubspot.crm().properties().core_api().get_all('CONTACTS')
    editable_properties = []
    for prop in all_properties.results:
        if prop.type == 'string' and prop.modification_metadata.read_only_value is False:
            editable_properties.append(prop)
    editable_properties_names = [p.name for p in editable_properties]
    editable_properties_names.append('hubspot_owner_id')
    contact = hubspot.crm().contacts().basic_api().get_by_id(
        contact_id,
        properties=editable_properties_names,
    )
    editable_properties_dict = {p.name: p for p in editable_properties}
    editable_properties_dict['hubspot_owner_id'] = {'label': 'Contact Owner'}

    return render_template(
        'contacts/show.html',
        contact=contact,
        properties_dict=editable_properties_dict,
        owners=hubspot.crm().owners().get_all(),
    )


@module.route('/<contact_id>', methods=['POST'])
@auth_required
def update(contact_id):
    properties = SimplePublicObject(properties=request.form)
    hubspot = create_client()
    hubspot.crm().contacts().basic_api().update(contact_id, simple_public_object_input=properties)
    return redirect(request.url, code=302)


@module.route('/search')
@auth_required
def search():
    hubspot = create_client()
    search = request.args.get('search')

    filter = Filter(
        property_name='email',
        operator='EQ',
        value=search,
    )
    filter_group = FilterGroup(filters=[filter])
    public_object_search_request = PublicObjectSearchRequest(
        filter_groups=[filter_group],
    )
    contacts_page = hubspot.crm().contacts().search_api().do_search(
        public_object_search_request=public_object_search_request
    )

    return render_template('contacts/list.html', contacts=contacts_page.results, search=search)
