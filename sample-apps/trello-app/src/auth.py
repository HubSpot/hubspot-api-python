from flask import redirect, url_for
from functools import wraps
from helpers.oauth import is_authorized as is_hubspot_authorized
from helpers.trello import is_authorized as is_trello_authorized


def auth_required(func):
    @wraps(func)
    def check_authentication(*args, **kwargs):
        if not is_hubspot_authorized() or not is_trello_authorized():
            return redirect(url_for("oauth.login"))

        return func(*args, **kwargs)

    return check_authentication
