from flask import redirect
from functools import wraps
from helpers.oauth import is_authenticated


def oauth_required(func):
    @wraps(func)
    def check_authentication(*args, **kwargs):
        if not is_authenticated():
            return redirect('/oauth/login')

        return func(*args, **kwargs)

    return check_authentication
