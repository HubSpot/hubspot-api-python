from flask import Blueprint, render_template, redirect, request
from hubspot.utils.oauth import get_auth_url
import os
from helpers.oauth import save_tokens, get_redirect_uri
from helpers.hubspot import create_client

module = Blueprint("oauth", __name__)


@module.route("/login")
def login():
    return render_template("oauth/login.html")


@module.route("/authorize")
def authorize():
    auth_url = get_auth_url(
        scopes=("contacts",),
        client_id=os.environ.get("HUBSPOT_CLIENT_ID"),
        redirect_uri=get_redirect_uri(),
    )

    return redirect(auth_url)


@module.route("/callback")
def callback():
    hubspot = create_client()
    tokens_response = hubspot.auth.oauth.default_api.create_token(
        grant_type="authorization_code",
        code=request.args.get("code"),
        redirect_uri=get_redirect_uri(),
        client_id=os.environ.get("HUBSPOT_CLIENT_ID"),
        client_secret=os.environ.get("HUBSPOT_CLIENT_SECRET"),
    )
    save_tokens(tokens_response)

    return redirect("/")
