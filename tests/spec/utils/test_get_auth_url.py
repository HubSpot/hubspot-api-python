import urllib

from hubspot.utils.oauth import get_auth_url, AUTHORIZE_URL


DATA = {
    "client_id": "client_id",
    "redirect_uri": "http://localhost",
    "scope": ("contacts", "timeline"),
    "optional_scope": ("scope1", "scope3")
}


def test_get_auth_url__empty_scope():
    params = {
        "client_id": DATA["client_id"],
        "redirect_uri": DATA["redirect_uri"],

    }
    expected_url = f"{AUTHORIZE_URL}?{urllib.parse.urlencode(params, safe='',quote_via=urllib.parse.quote)}"

    result = get_auth_url(
        DATA["client_id"],
        DATA["redirect_uri"]
    )

    assert result == expected_url


def test_get_auth_url__scope():
    params = {
        "client_id": DATA["client_id"],
        "redirect_uri": DATA["redirect_uri"],
        "scope": " ".join(DATA["scope"]),
    }
    expected_url = f"{AUTHORIZE_URL}?{urllib.parse.urlencode(params, safe='', quote_via=urllib.parse.quote)}"

    result = get_auth_url(
        DATA["client_id"],
        DATA["redirect_uri"],
        DATA["scope"]
    )

    assert result == expected_url


def test_get_auth_url__optional_scope():
    params = {
        "client_id": DATA["client_id"],
        "redirect_uri": DATA["redirect_uri"],
        "optional_scope": " ".join(DATA["optional_scope"]),
    }
    expected_url = f"{AUTHORIZE_URL}?{urllib.parse.urlencode(params, safe='', quote_via=urllib.parse.quote)}"

    result = get_auth_url(
        DATA["client_id"],
        DATA["redirect_uri"],
        optional_scope=DATA["optional_scope"]
    )

    assert result == expected_url


def test_get_auth_url__state():

    params = {
        "client_id": DATA["client_id"],
        "redirect_uri": DATA["redirect_uri"],
        "scope": " ".join(DATA["scope"]),
        "optional_scope": " ".join(DATA["optional_scope"]),
        "state": "test_state"
    }
    expected_url = f"{AUTHORIZE_URL}?{urllib.parse.urlencode(params, safe='', quote_via=urllib.parse.quote)}"

    result = get_auth_url(
        DATA["client_id"],
        DATA["redirect_uri"],
        DATA["scope"],
        DATA["optional_scope"],
        state=params["state"]
    )

    assert result == expected_url
