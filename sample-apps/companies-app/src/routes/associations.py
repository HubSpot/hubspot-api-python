from flask import Blueprint, render_template, request, redirect, url_for
from hubspot.crm.contacts import PublicObjectSearchRequest, Filter, FilterGroup, SimplePublicObject, SimplePublicObjectInput
from hubspot.crm.associations import BatchInputPublicObjectId, BatchInputPublicAssociation, PublicAssociation
from hubspot.crm.contacts import BatchReadInputSimplePublicObjectId, SimplePublicObjectId
from hubspot.crm import ObjectType
from helpers.hubspot import create_client
from auth import auth_required


module = Blueprint('associations', __name__)


@module.route('/company/<company_id>/contacts')
@auth_required
def list(company_id):
    hubspot = create_client()
    company = hubspot.crm().companies().basic_api().get_by_id(company_id)

    associations = hubspot.crm().associations().batch_api().read_batch(
        ObjectType.COMPANIES,
        ObjectType.CONTACTS,
        batch_input_public_object_id=BatchInputPublicObjectId(inputs=[company_id])
    )
    inputs = []
    if associations.results:
        inputs = [SimplePublicObjectId(id=contact.id) for contact in associations.results[0].to]
    associated_contacts = hubspot.crm().contacts().batch_api().read_batch(
        batch_read_input_simple_public_object_id=BatchReadInputSimplePublicObjectId(inputs=inputs)
    )

    return render_template(
        'associations/list.html',
        company=company,
        associated_contacts=associated_contacts.results
    )


@module.route('/company/<company_id>/contacts/new')
@auth_required
def new(company_id):
    hubspot = create_client()

    company = hubspot.crm().companies().basic_api().get_by_id(company_id)

    search_request = PublicObjectSearchRequest(sorts=[{
        'propertyName': 'createdate',
        'direction': 'DESCENDING',
    }])

    search = request.args.get('search')
    if search:
        print(search, flush=True)
        filter = Filter(
            property_name='email',
            operator='EQ',
            value=search,
        )
        search_request.filter_groups = [FilterGroup(filters=[filter])]

    contacts_page = hubspot.crm().contacts().search_api().do_search(public_object_search_request=search_request)

    return render_template(
        'associations/new.html',
        search=search,
        company=company,
        contacts=contacts_page.results
    )


@module.route('/company/<company_id>/contacts/<contact_id>/create')
@auth_required
def create(company_id, contact_id):
    hubspot = create_client()
    association = PublicAssociation(
        _from=company_id,
        to=contact_id,
    )
    batch_input_public_association = BatchInputPublicAssociation(
        inputs=[association]
    )
    hubspot.crm().associations().batch_api().create_batch(
        ObjectType.COMPANIES,
        ObjectType.CONTACTS,
        batch_input_public_association=batch_input_public_association,
    )

    return redirect(url_for('associations.list', company_id=company_id))


@module.route('/company/<company_id>/contacts/<contact_id>/delete')
@auth_required
def delete(company_id, contact_id):
    hubspot = create_client()
    association = PublicAssociation(
        _from=company_id,
        to=contact_id,
    )
    batch_input_public_association = BatchInputPublicAssociation(
        inputs=[association]
    )
    hubspot.crm().associations().batch_api().archive_batch(
        ObjectType.COMPANIES,
        ObjectType.CONTACTS,
        batch_input_public_association=batch_input_public_association,
    )

    return redirect(url_for('associations.list', company_id=company_id))
