from flask import Blueprint, render_template, redirect, request
import hubspot
from hubspot.utils.oauth import get_auth_url
import os
import json
from helpers.oauth import save_tokens

module = Blueprint(__name__, __name__)


@module.route('/')
@module.route('/oauth/login')
def login():
    return render_template('oauth/login.html')


@module.route('/oauth/authorize')
def authorize():
    auth_url = get_auth_url(
        scopes=('contacts',),
        client_id=os.environ.get('HUBSPOT_CLIENT_ID'),
        redirect_uri=request.url_root + 'oauth/callback',
    )

    return redirect(auth_url)


@module.route('/oauth/callback')
def callback():
    tokens_response = hubspot.Client.create().auth().oauth().default_api().create_token(
        grant_type='authorization_code',
        code=request.args.get('code'),
        redirect_uri=request.url_root + 'oauth/callback',
        client_id=os.environ.get('HUBSPOT_CLIENT_ID'),
        client_secret=os.environ.get('HUBSPOT_CLIENT_SECRET'),
    )

    tokens = save_tokens(tokens_response)

    return json.dumps(tokens)
