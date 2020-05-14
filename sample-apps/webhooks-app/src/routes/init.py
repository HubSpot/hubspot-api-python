from flask import Blueprint, render_template, redirect, url_for
from auth import auth_required


module = Blueprint("init", __name__)


@module.route("/")
@auth_required
def start():
    return redirect(url_for("init.step_1"))


@module.route("/step-1")
@auth_required
def step_1():
    return render_template("init/step_1.html")
