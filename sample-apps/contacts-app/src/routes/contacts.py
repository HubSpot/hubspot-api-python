import io, csv
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session
from helpers.hubspot import create_client
from helpers.session import SessionKey
from auth import auth_required
from hubspot.crm import ObjectType
from hubspot.crm.contacts import PublicObjectSearchRequest, SimplePublicObject, SimplePublicObjectInput, Filter, FilterGroup

module = Blueprint('contacts', __name__)


@module.route('/')
@auth_required
def list():
    hubspot = create_client()
    search_request = PublicObjectSearchRequest(sorts=[{
        'propertyName': 'createdate',
        'direction': 'DESCENDING',
    }])
    contacts_page = hubspot.crm().contacts().search_api().do_search(public_object_search_request=search_request)

    return render_template(
        'contacts/list.html',
        contacts=contacts_page.results,
        action_performed=session.pop(SessionKey.ACTION_PERFORMED, None),
    )


@module.route('/new')
@auth_required
def new():
    contact = SimplePublicObject(properties={
        'email': None,
    })
    properties_dict = {
        'email': {'label': 'Email'},
    }

    return render_template('contacts/show.html', contact=contact, properties_dict=properties_dict)


@module.route('/<contact_id>')
@auth_required
def show(contact_id):
    hubspot = create_client()
    all_properties = hubspot.crm().properties().core_api().get_all(ObjectType.CONTACTS)
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
        action_performed=session.pop(SessionKey.ACTION_PERFORMED, None),
    )


@module.route('/new', methods=['POST'])
@auth_required
def create():
    properties = SimplePublicObjectInput(request.form)
    hubspot = create_client()
    contact = hubspot.crm().contacts().basic_api().create(simple_public_object_input=properties)
    session[SessionKey.ACTION_PERFORMED] = 'created'
    return redirect(url_for('contacts.show', contact_id=contact.id))


@module.route('/<contact_id>', methods=['POST'])
@auth_required
def update(contact_id):
    properties = SimplePublicObject(properties=request.form)
    hubspot = create_client()
    hubspot.crm().contacts().basic_api().update(contact_id, simple_public_object_input=properties)
    session[SessionKey.ACTION_PERFORMED] = 'updated'
    return redirect(request.url)


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


@module.route('/delete/<contact_id>')
@auth_required
def delete(contact_id):
    hubspot = create_client()
    hubspot.crm().contacts().basic_api().archive(contact_id)
    session[SessionKey.ACTION_PERFORMED] = 'deleted'
    return redirect(url_for('contacts.list'))


@module.route('/export')
@auth_required
def export():
    si = io.StringIO()
    writer = csv.writer(si)
    writer.writerow(['Email', 'Firstname', 'Lastname'])

    hubspot = create_client()
    contacts = hubspot.crm().contacts().get_all()
    for contact in contacts:
        writer.writerow([
            contact.properties['email'],
            contact.properties['firstname'],
            contact.properties['lastname'],
        ])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=contacts.csv"
    output.headers["Content-type"] = "text/csv"
    return output

