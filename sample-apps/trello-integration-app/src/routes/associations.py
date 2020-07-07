from flask import Blueprint, render_template, url_for, redirect
from auth import auth_required

module = Blueprint("associations", __name__)


@module.route("/", methods=["GET"])
@auth_required
def list():
    return render_template(
        "associations/list.html",
    )
