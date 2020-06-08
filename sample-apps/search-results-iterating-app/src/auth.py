from flask import redirect, url_for
from functools import wraps
from helpers.oauth import is_authenticated


def auth_required(func):
    @wraps(func)
    def check_authentication(*args, **kwargs):
        if not is_authenticated():
            return redirect(url_for("oauth.login"))

        return func(*args, **kwargs)

    return check_authentication
