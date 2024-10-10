from hubspot import HubSpot
from hubspot.auth.oauth import AccessTokensApi, RefreshTokensApi, TokensApi


def test_is_discoverable():
    proxy = "https://localhost:9000"
    proxy_headers = {'x': 'y'}

    api_client = HubSpot(proxy=proxy, proxy_headers=proxy_headers)
    
    assert "proxy" in api_client.config
    assert "proxy_headers" in api_client.config
    
    assert api_client.config["proxy"] == proxy
    assert api_client.config["proxy_headers"] == proxy_headers

    apis = api_client.auth.oauth

    assert "proxy" in apis.config
    assert "proxy_headers" in apis.config
    
    assert apis.config["proxy"] == proxy
    assert apis.config["proxy_headers"] == proxy_headers