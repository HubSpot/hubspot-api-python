from flask import Blueprint, render_template
from auth import auth_required
from helpers.hubspot import create_client


module = Blueprint("readme", __name__)


@module.route("/")
@auth_required
def readme():
    hubspot = create_client()
    hubspot.crm.contacts.basic_api.get_page()
    return render_template("readme/readme.html")
