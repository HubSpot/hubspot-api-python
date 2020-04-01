import hubspot.crm.timeline as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    def events_api(self) -> api_client.EventsApi:
        return self._configure_api_client(api_client, 'EventsApi')

    def templates_api(self) -> api_client.TemplatesApi:
        return self._configure_api_client(api_client, 'TemplatesApi')

    def tokens_api(self) -> api_client.TokensApi:
        return self._configure_api_client(api_client, 'TokensApi')
