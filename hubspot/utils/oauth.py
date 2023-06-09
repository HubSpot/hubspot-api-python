import urllib

AUTHORIZE_URL = "https://app.hubspot.com/oauth/authorize"


def get_auth_url(
    client_id: str,
    redirect_uri: str,
    scope: tuple = None,
    optional_scope: tuple = None,
    state: str = None
) -> str:
    query_params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri
    }

    if scope:
        query_params["scope"] = " ".join(scope)
    if optional_scope:
        query_params["optional_scope"] = " ".join(optional_scope)
    if state:
        query_params.setdefault("state", state)

    params = urllib.parse.urlencode(
        query_params,
        safe='',
        quote_via=urllib.parse.quote,
    )

    return f"{AUTHORIZE_URL}?{params}"
