from ..discovery_base import DiscoveryBase
from .associations.discovery import Discovery as AssociationsDiscovery
from .companies.discovery import Discovery as CompaniesDiscovery
from .contacts.discovery import Discovery as ContactsDiscovery
from .deals.discovery import Discovery as DealsDiscovery
from .extensions.discovery import Discovery as ExtensionsDiscovery
from .imports.discovery import Discovery as ImportsDiscovery
from .line_items.discovery import Discovery as LineItemsDiscovery
from .pipelines.discovery import Discovery as PipelinesDiscovery
from .products.discovery import Discovery as ProductsDiscovery
from .properties.discovery import Discovery as PropertiesDiscovery
from .quotes.discovery import Discovery as QuotesDiscovery
from .owners.discovery import Discovery as OwnersDiscovery
from .tickets.discovery import Discovery as TicketsDiscovery
from .timeline.discovery import Discovery as TimelineDiscovery


class Discovery(DiscoveryBase):
    def associations(self):
        return AssociationsDiscovery(self.config)

    def contacts(self):
        return ContactsDiscovery(self.config)

    def companies(self):
        return CompaniesDiscovery(self.config)

    def deals(self):
        return DealsDiscovery(self.config)

    def extensions(self):
        return ExtensionsDiscovery(self.config)

    def imports(self):
        return ImportsDiscovery(self.config)

    def line_items(self):
        return LineItemsDiscovery(self.config)

    def pipelines(self):
        return PipelinesDiscovery(self.config)
   
    def products(self):
        return ProductsDiscovery(self.config)

    def properties(self):
        return PropertiesDiscovery(self.config)

    def quotes(self):
        return QuotesDiscovery(self.config)

    def owners(self):
        return OwnersDiscovery(self.config)

    def tickets(self):
        return TicketsDiscovery(self.config)

    def timeline(self):
        return TimelineDiscovery(self.config)

