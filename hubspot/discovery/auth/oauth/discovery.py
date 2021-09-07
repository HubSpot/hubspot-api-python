import hubspot.auth.oauth as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def access_tokens_api(self) -> api_client.AccessTokensApi:
        return self._configure_api_client(api_client, "AccessTokensApi")

    @property
    def refresh_tokens_api(self) -> api_client.RefreshTokensApi:
        return self._configure_api_client(api_client, "RefreshTokensApi")

    @property
    def tokens_api(self) -> api_client.TokensApi:
        return self._configure_api_client(api_client, "TokensApi")
