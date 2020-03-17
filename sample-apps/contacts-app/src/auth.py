import os
from flask import redirect, url_for
from functools import wraps
from helpers.oauth import is_authenticated as is_oauth_authenticated


def is_authenticated():
    if is_oauth_authenticated():
        return True
    api_key = os.environ.get('HUBSPOT_API_KEY')
    return api_key is not None


def auth_required(func):
    @wraps(func)
    def check_authentication(*args, **kwargs):
        if not is_authenticated():
            return redirect(url_for('oauth.login'))

        return func(*args, **kwargs)

    return check_authentication
