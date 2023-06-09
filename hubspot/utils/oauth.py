import urllib

AUTHORIZE_URL = "https://app.hubspot.com/oauth/authorize"


def get_auth_url(
    client_id: str,
    redirect_uri: str,
    scopes: tuple = None,
    optional_scopes: tuple = None,
):
    query_params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri
    }

    if scopes:
        query_params["scope"] = ' '.join(scopes)

    if optional_scopes:
        query_params["optional_scope"] = ' '.join(optional_scopes)

    params = urllib.parse.urlencode(
        query_params,
        safe='',
        quote_via=urllib.parse.quote,
    )

    return f"{AUTHORIZE_URL}?{params}&state="
