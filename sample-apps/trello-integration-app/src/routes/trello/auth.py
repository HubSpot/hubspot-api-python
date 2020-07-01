from flask import Blueprint, redirect, url_for
import os
from helpers.trello import get_auth_url, save_token

module = Blueprint("trello.auth", __name__)


@module.route("/authorize")
def authorize():
    auth_url = get_auth_url(
        key=os.environ.get("TRELLO_API_KEY"),
        return_url=url_for("trello.auth.callback", response="callback", _external=True),
    )

    return redirect(auth_url)


@module.route("/token/<token>/", methods=["GET"])
def set_token(token):
    save_token(token)

    return redirect(url_for("home"))


@module.route("/<response>", methods=["GET"])
def callback(response):
    return """<script type="text/javascript">
                var token = window.location.href.split("token=")[1];
                window.location = "/trello/auth/token/" + token;
            </script>"""
