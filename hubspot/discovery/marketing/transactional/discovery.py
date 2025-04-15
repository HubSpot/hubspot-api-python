import hubspot.marketing.transactional as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def public_smtp_tokens_api(self) -> api_client.PublicSMTPTokensApi:
        return self._configure_api_client(api_client, "PublicSMTPTokensApi")

    @property
    def single_send_api(self) -> api_client.SingleSendApi:
        return self._configure_api_client(api_client, "SingleSendApi")
