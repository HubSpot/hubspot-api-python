from flask import Blueprint
from auth import auth_required


module = Blueprint("events", __name__)


@module.route("/")
@auth_required
def list():
    pass
