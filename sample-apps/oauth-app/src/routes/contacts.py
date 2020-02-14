from flask import Blueprint, render_template
from helpers.hubspot import create_client
from auth import oauth_required


module = Blueprint(__name__, __name__)


@module.route('/')
@module.route('/contacts')
@oauth_required
def contacts():
    hubspot = create_client()
    contacts_page = hubspot.crm().contacts().basic_api().get_page()

    return render_template('contacts/list.html', contacts=contacts_page.results)
