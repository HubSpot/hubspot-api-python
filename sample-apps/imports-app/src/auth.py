from flask import redirect, url_for
from functools import wraps
from helpers.oauth import is_authorized


def auth_required(func):
    @wraps(func)
    def check_auth(*args, **kwargs):
        if not is_authorized():
            return redirect(url_for("oauth.login"))

        return func(*args, **kwargs)

    return check_auth
