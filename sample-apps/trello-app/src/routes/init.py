from flask import Blueprint, render_template
from auth import auth_required

module = Blueprint("init", __name__)


@module.route("/extension")
@auth_required
def extension():
    return render_template(
        "init/extension.html",
    )
