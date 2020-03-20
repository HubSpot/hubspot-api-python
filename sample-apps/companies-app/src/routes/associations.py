from flask import Blueprint, render_template, request, redirect, url_for
from hubspot.crm.companies import PublicObjectSearchRequest, Filter, FilterGroup, SimplePublicObject, SimplePublicObjectInput
from hubspot.crm.associations import BatchInputPublicObjectId
from hubspot.crm.contacts import BatchReadInputSimplePublicObjectId, SimplePublicObjectId
from hubspot.crm import ObjectType
from helpers.hubspot import create_client
from auth import auth_required


module = Blueprint('associations', __name__)


@module.route('/company/<company_id>/contacts')
@auth_required
def company_to_contacts(company_id):
    hubspot = create_client()
    company = hubspot.crm().companies().basic_api().get_by_id(company_id)

    associations = hubspot.crm().associations().batch_api().read_batch(
        ObjectType.COMPANIES,
        ObjectType.CONTACTS,
        batch_input_public_object_id=BatchInputPublicObjectId(inputs=[company_id])
    )
    inputs = [SimplePublicObjectId(id=contact.id) for contact in associations.results[0].to]
    associated_contacts = hubspot.crm().contacts().batch_api().read_batch(
        batch_read_input_simple_public_object_id=BatchReadInputSimplePublicObjectId(inputs=inputs)
    )
    print(associated_contacts.results, flush=True)

    return render_template('associations/list.html', company=company, associated_contacts=associated_contacts.results)
