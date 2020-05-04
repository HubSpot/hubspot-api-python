from flask import Blueprint, render_template, request, redirect, url_for, session
from hubspot.crm.contacts import PublicObjectSearchRequest, Filter, FilterGroup
from hubspot.crm.associations import (
    BatchInputPublicObjectId,
    BatchInputPublicAssociation,
    PublicAssociation,
    PublicObjectId,
)
from hubspot.crm.contacts import (
    BatchReadInputSimplePublicObjectId,
    SimplePublicObjectId,
)
from hubspot.crm import ObjectType, AssociationType
from helpers.hubspot import create_client
from helpers.session import SessionKey
from auth import auth_required


module = Blueprint("associations", __name__)


@module.route("/company/<company_id>/contacts")
@auth_required
def list(company_id):
    hubspot = create_client()
    company = hubspot.crm.companies.basic_api.get_by_id(company_id)

    associations = hubspot.crm.associations.batch_api.read(
        ObjectType.COMPANIES,
        ObjectType.CONTACTS,
        batch_input_public_object_id=BatchInputPublicObjectId(inputs=[company_id]),
    )
    inputs = []
    if associations.results:
        inputs = [
            SimplePublicObjectId(id=contact.id)
            for contact in associations.results[0].to
        ]
    associated_contacts = hubspot.crm.contacts.batch_api.read(
        batch_read_input_simple_public_object_id=BatchReadInputSimplePublicObjectId(
            inputs=inputs
        )
    )

    return render_template(
        "associations/list.html",
        company=company,
        associated_contacts=associated_contacts.results,
        action_performed=session.pop(SessionKey.ACTION_PERFORMED, None),
    )


@module.route("/company/<company_id>/contacts/new")
@auth_required
def new(company_id):
    hubspot = create_client()

    company = hubspot.crm.companies.basic_api.get_by_id(company_id)

    search_request = PublicObjectSearchRequest(
        sorts=[{"propertyName": "createdate", "direction": "DESCENDING",}]
    )

    search = request.args.get("search")
    if search:
        filter = Filter(property_name="email", operator="EQ", value=search,)
        search_request.filter_groups = [FilterGroup(filters=[filter])]

    contacts_page = hubspot.crm.contacts.search_api.do_search(
        public_object_search_request=search_request
    )

    return render_template(
        "associations/new.html",
        search=search,
        company=company,
        contacts=contacts_page.results,
    )


@module.route("/company/<company_id>/contact/<contact_id>/create")
@auth_required
def create(company_id, contact_id):
    hubspot = create_client()
    association = PublicAssociation(
        _from=PublicObjectId(id=company_id),
        to=PublicObjectId(id=contact_id),
        type=AssociationType.COMPANY_TO_CONTACT,
    )
    batch_input_public_association = BatchInputPublicAssociation(inputs=[association])
    hubspot.crm.associations.batch_api.create(
        ObjectType.COMPANIES,
        ObjectType.CONTACTS,
        batch_input_public_association=batch_input_public_association,
    )
    session[SessionKey.ACTION_PERFORMED] = "created"

    return redirect(url_for("associations.list", company_id=company_id))


@module.route("/company/<company_id>/contact/<contact_id>/delete")
@auth_required
def delete(company_id, contact_id):
    hubspot = create_client()
    association = PublicAssociation(
        _from=PublicObjectId(id=company_id),
        to=PublicObjectId(id=contact_id),
        type=AssociationType.COMPANY_TO_CONTACT,
    )
    batch_input_public_association = BatchInputPublicAssociation(inputs=[association])
    hubspot.crm.associations.batch_api.archive(
        ObjectType.COMPANIES,
        ObjectType.CONTACTS,
        batch_input_public_association=batch_input_public_association,
    )
    session[SessionKey.ACTION_PERFORMED] = "deleted"

    return redirect(url_for("associations.list", company_id=company_id))
