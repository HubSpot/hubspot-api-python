from flask import Blueprint, render_template
from auth import auth_required


module = Blueprint("imports", __name__)


@module.route("/")
@auth_required
def readme():
    return render_template("imports/readme.html")
