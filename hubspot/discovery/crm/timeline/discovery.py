import hubspot.crm.timeline as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def events_api(self) -> api_client.EventsApi:
        return self._configure_api_client(api_client, "EventsApi")

    @property
    def templates_api(self) -> api_client.TemplatesApi:
        return self._configure_api_client(api_client, "TemplatesApi")

    @property
    def tokens_api(self) -> api_client.TokensApi:
        return self._configure_api_client(api_client, "TokensApi")
