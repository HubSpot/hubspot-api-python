from flask import Blueprint, render_template, request, redirect
from helpers.hubspot import create_client
from auth import oauth_required
from pprint import pprint
from hubspot.crm.contacts import PublicObjectSearchRequest, SimplePublicObject, Filter, FilterGroup

module = Blueprint(__name__, __name__)


@module.route('/')
@oauth_required
def list():
    hubspot = create_client()
    contacts_page = hubspot.crm().contacts().basic_api().get_page()

    return render_template('contacts/list.html', contacts=contacts_page.results)


@module.route('/<contact_id>')
@oauth_required
def show(contact_id):
    pprint(__name__)
    hubspot = create_client()
    all_properties = hubspot.crm().properties().core_api().get_all('CONTACTS')
    editable_properties = []
    for p in all_properties.results:
        if p.type == 'string' and p.modification_metadata.read_only_value is False:
            editable_properties.append(p)
    contact = hubspot.crm().contacts().basic_api().get_by_id(
        contact_id,
        properties=[p.name for p in editable_properties],
    )
    editable_properties_dict = {p.name: p for p in editable_properties}
    return render_template('contacts/show.html', contact=contact, properties_dict=editable_properties_dict)


@module.route('/<contact_id>', methods=['POST'])
@oauth_required
def update(contact_id):
    properties = SimplePublicObject(properties=request.form)
    hubspot = create_client()
    hubspot.crm().contacts().basic_api().update(contact_id, simple_public_object_input=properties)
    return redirect(request.url, code=302)


@module.route('/search')
@oauth_required
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
