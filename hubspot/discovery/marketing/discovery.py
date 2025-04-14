from ..discovery_base import DiscoveryBase

class Discovery(DiscoveryBase):
    @property
    def emails(self):
        from .emails.discovery import Discovery as EmailsDiscovery
        return EmailsDiscovery(self.config)

    @property
    def events(self):
        from .events.discovery import Discovery as EventsDiscovery
        return EventsDiscovery(self.config)

    @property
    def forms(self):
        from .forms.discovery import Discovery as FormsDiscovery
        return FormsDiscovery(self.config)

    @property
    def transactional(self):
        from .transactional.discovery import Discovery as TransactionalDiscovery
        return TransactionalDiscovery(self.config)
