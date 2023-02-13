import hubspot.crm.extensions.cards as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def cards_api(self) -> api_client.CardsApi:
        return self._configure_api_client(api_client, "CardsApi")

    @property
    def sample_response_api(self) -> api_client.SampleResponseApi:
        return self._configure_api_client(api_client, "SampleResponseApi")
