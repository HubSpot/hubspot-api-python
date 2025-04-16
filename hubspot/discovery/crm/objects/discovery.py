import hubspot.crm.objects as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def basic_api(self) -> api_client.BasicApi:
        return self._configure_api_client(api_client, "BasicApi")

    @property
    def batch_api(self) -> api_client.BatchApi:
        return self._configure_api_client(api_client, "BatchApi")

    @property
    def search_api(self) -> api_client.SearchApi:
        return self._configure_api_client(api_client, "SearchApi")

    @property
    def calls(self):
        from .calls.discovery import Discovery as CallsDiscovery
        return CallsDiscovery(self.config)

    @property
    def communications(self):
        from .communications.discovery import Discovery as CommunicationsDiscovery
        return CommunicationsDiscovery(self.config)

    @property
    def deal_splits(self):
        from .deal_splits.discovery import Discovery as DealSplitsDiscovery
        return DealSplitsDiscovery(self.config)

    @property
    def emails(self):
        from .emails.discovery import Discovery as EmailsDiscovery
        return EmailsDiscovery(self.config)

    @property
    def feedback_submissions(self):
        from .feedback_submissions.discovery import Discovery as FeedbackSubmissionsDiscovery
        return FeedbackSubmissionsDiscovery(self.config)

    @property
    def goals(self):
        from .goals.discovery import Discovery as GoalsDiscovery
        return GoalsDiscovery(self.config)

    @property
    def leads(self):
        from .leads.discovery import Discovery as LeadsDiscovery
        return LeadsDiscovery(self.config)

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

    @property
    def taxes(self):
        from .taxes.discovery import Discovery as TaxesDiscovery
        return TaxesDiscovery(self.config)

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
