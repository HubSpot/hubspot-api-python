import hubspot.marketing.emails as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def marketing_emails_api(self) -> api_client.MarketingEmailsApi:
        return self._configure_api_client(api_client, "MarketingEmailsApi")

    @property
    def statistics_api(self) -> api_client.StatisticsApi:
        return self._configure_api_client(api_client, "StatisticsApi")
