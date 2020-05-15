from flask import Blueprint
from auth import auth_required


module = Blueprint("webhooks", __name__)


@module.route("/handle", methods=["POST"])
@auth_required
def handle():
    pass
