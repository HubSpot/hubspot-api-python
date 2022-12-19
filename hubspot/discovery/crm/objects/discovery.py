import hubspot.crm.objects as api_client
from ...discovery_base import DiscoveryBase

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
    def public_object_api(self) -> api_client.PublicObjectApi:
        return self._configure_api_client(api_client, "PublicObjectApi")

    @property
    def calls(self):
        from .calls.discovery import Discovery as CallsDiscovery
        return CallsDiscovery(self.config)

    @property
    def emails(self):
        from .emails.discovery import Discovery as EmailsDiscovery
        return EmailsDiscovery(self.config)

    @property
    def feedback_submissions(self):
        from .feedback_submissions.discovery import Discovery as FeedbackSubmissionsDiscovery
        return FeedbackSubmissionsDiscovery(self.config)

    @property
    def meetings(self):
        from .meetings.discovery import Discovery as MeetingsDiscovery
        return MeetingsDiscovery(self.config)

    @property
    def notes(self):
        from .notes.discovery import Discovery as NotesDiscovery
        return NotesDiscovery(self.config)

    @property
    def postal_mail(self):
        from .postal_mail.discovery import Discovery as PostalMailDiscovery
        return PostalMailDiscovery(self.config)

    @property
    def tasks(self):
        from .tasks.discovery import Discovery as TasksDiscovery
        return TasksDiscovery(self.config)

    def get_all(self, object_type, **kwargs):
        return self.fetch_all(object_type, **kwargs)

    def fetch_all(self, object_type, **kwargs):
        results = []
        after = None
        PAGE_MAX_SIZE = 100

        while True:
            page = self.basic_api.get_page(object_type, after=after, limit=PAGE_MAX_SIZE, **kwargs)
            results.extend(page.results)
            if page.paging is None:
                break
            after = page.paging.next.after

        return results
