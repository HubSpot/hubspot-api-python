from flask import Blueprint, render_template, request, redirect, url_for
from hubspot.crm.companies import PublicObjectSearchRequest, Filter, FilterGroup, SimplePublicObject, SimplePublicObjectInput
from helpers.hubspot import create_client
from auth import auth_required


module = Blueprint('companies', __name__)


@module.route('/')
@auth_required
def list():
    hubspot = create_client()
    search_request = PublicObjectSearchRequest(sorts=[{
        'propertyName': 'createdate',
        'direction': 'DESCENDING',
    }])
    companies_page = hubspot.crm().companies().search_api().do_search(public_object_search_request=search_request)

    return render_template('companies/list.html', companies=companies_page.results)


@module.route('/new')
@auth_required
def new():
    return render_template('companies/show.html', company=SimplePublicObject())


@module.route('/new', methods=['POST'])
@auth_required
def create():
    properties = SimplePublicObjectInput(properties=request.form)
    hubspot = create_client()
    company = hubspot.crm().companies().basic_api().create(simple_public_object_input=properties)
    return redirect(url_for('companies.show', company_id=company.id))


@module.route('/<company_id>')
@auth_required
def show(company_id):
    hubspot = create_client()
    company = hubspot.crm().companies().basic_api().get_by_id(company_id)
    return render_template('companies/show.html', company=company)


@module.route('/<company_id>', methods=['POST'])
@auth_required
def update(company_id):
    properties = SimplePublicObjectInput(properties=request.form)
    hubspot = create_client()
    company = hubspot.crm().companies().basic_api().update(company_id, simple_public_object_input=properties)
    return redirect(url_for('companies.show', company_id=company.id))


@module.route('/search')
@auth_required
def search():
    hubspot = create_client()
    search = request.args.get('search')

    from pprint import pprint

    pprint(search)

    filter = Filter(
        property_name='domain',
        operator='EQ',
        value=search,
    )
    filter_group = FilterGroup(filters=[filter])
    public_object_search_request = PublicObjectSearchRequest(
        filter_groups=[filter_group],
    )
    companies_page = hubspot.crm().companies().search_api().do_search(
        public_object_search_request=public_object_search_request
    )

    return render_template('companies/list.html', companies=companies_page.results, search=search)


@module.route('/delete/<company_id>')
@auth_required
def delete(company_id):
    hubspot = create_client()
    hubspot.crm().companies().basic_api().archive(company_id)
    return redirect(url_for('companies.list'))

