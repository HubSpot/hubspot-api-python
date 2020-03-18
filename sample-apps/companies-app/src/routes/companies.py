from flask import Blueprint, render_template, request
from hubspot.crm.companies import PublicObjectSearchRequest, Filter, FilterGroup
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
