from ..discovery_base import DiscoveryBase
from .events.discovery import Discovery as EventsDiscovery
from .forms.discovery import Discovery as FormsDiscovery
from .transactional.discovery import Discovery as TransactionalDiscovery


class Discovery(DiscoveryBase):
    @property
    def events(self):
        return EventsDiscovery(self.config)

    @property
    def forms(self):
        return FormsDiscovery(self.config)

    @property
    def transactional(self):
        return TransactionalDiscovery(self.config)
