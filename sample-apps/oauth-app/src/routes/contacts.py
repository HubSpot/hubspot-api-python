from flask import Blueprint, render_template, redirect
from helpers.hubspot import create_client
from helpers.oauth import is_authenticated


module = Blueprint(__name__, __name__)


@module.route('/')
@module.route('/contacts')
def contacts():
    if not is_authenticated():
        return redirect('/oauth/login')

    hubspot = create_client()
    contacts_page = hubspot.crm().contacts().basic_api().get_page()

    print(contacts)
    return render_template('contacts/list.html', contacts=contacts_page.results)
