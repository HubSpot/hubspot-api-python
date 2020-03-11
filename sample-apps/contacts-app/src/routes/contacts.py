from flask import Blueprint, render_template, request
from helpers.hubspot import create_client
from auth import oauth_required
from hubspot.crm.contacts import PublicObjectSearchRequest, Filter, FilterGroup

module = Blueprint(__name__, __name__)


@module.route('/')
@oauth_required
def contacts():
    hubspot = create_client()
    contacts_page = hubspot.crm().contacts().basic_api().get_page()

    return render_template('contacts/list.html', contacts=contacts_page.results)


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
