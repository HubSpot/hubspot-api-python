from flask import session


def get_auth_url(key: str, return_url: str, name="HubSpot", expiration="30days", scope="read", response_type="token"):
    return "https://trello.com/1/authorize?key={}&name={}&expiration={}&response_type={}&scope={}&return_url={}".format(
        key, name, expiration, response_type, scope, return_url
    )


TOKEN_KEY = "trello_token"


def save_token(token):
    session[TOKEN_KEY] = token

    return token


def is_authorized():
    return TOKEN_KEY in session


def get_token():
    return session[TOKEN_KEY]
