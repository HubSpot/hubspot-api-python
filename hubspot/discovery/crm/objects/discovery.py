import hubspot.crm.objects as api_client
from ...discovery_base import DiscoveryBase
from .feedback_submissions.discovery import Discovery as FeedbackSubmissionsDiscovery


class Discovery(DiscoveryBase):
    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def associations_api(self) -> api_client.AssociationsApi:
        return self._configure_api_client(api_client, "AssociationsApi")

    @property
    def search_api(self) -> api_client.SearchApi:
        return self._configure_api_client(api_client, "SearchApi")

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def gdpr_api(self) -> api_client.GDPRApi:
        return self._configure_api_client(api_client, "GDPRApi")

    @property
    def feedback_submissions(self):
        return FeedbackSubmissionsDiscovery(self.config)
