from flask import Blueprint, render_template
from helpers.hubspot import create_client
from auth import auth_required


module = Blueprint('companies', __name__)


@module.route('/')
@auth_required
def list():
    return render_template('companies/list.html')
