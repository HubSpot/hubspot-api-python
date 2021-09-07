from hubspot import HubSpot
from hubspot.auth.oauth import AccessTokensApi, RefreshTokensApi, TokensApi


def test_is_discoverable():
    apis = HubSpot().auth.oauth
    assert isinstance(apis.access_tokens_api, AccessTokensApi)
    assert isinstance(apis.refresh_tokens_api, RefreshTokensApi)
    assert isinstance(apis.tokens_api, TokensApi)
