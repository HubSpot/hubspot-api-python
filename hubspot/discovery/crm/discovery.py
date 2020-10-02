from ..discovery_base import DiscoveryBase
from .associations.discovery import Discovery as AssociationsDiscovery
from .companies.discovery import Discovery as CompaniesDiscovery
from .contacts.discovery import Discovery as ContactsDiscovery
from .deals.discovery import Discovery as DealsDiscovery
from .extensions.discovery import Discovery as ExtensionsDiscovery
from .imports.discovery import Discovery as ImportsDiscovery
from .line_items.discovery import Discovery as LineItemsDiscovery
from .objects.discovery import Discovery as ObjectsDiscovery
from .owners.discovery import Discovery as OwnersDiscovery
from .pipelines.discovery import Discovery as PipelinesDiscovery
from .products.discovery import Discovery as ProductsDiscovery
from .properties.discovery import Discovery as PropertiesDiscovery
from .quotes.discovery import Discovery as QuotesDiscovery
from .schemas.discovery import Discovery as SchemasDiscovery
from .tickets.discovery import Discovery as TicketsDiscovery
from .timeline.discovery import Discovery as TimelineDiscovery


class Discovery(DiscoveryBase):
    @property
    def associations(self):
        return AssociationsDiscovery(self.config)

    @property
    def contacts(self):
        return ContactsDiscovery(self.config)

    @property
    def companies(self):
        return CompaniesDiscovery(self.config)

    @property
    def deals(self):
        return DealsDiscovery(self.config)

    @property
    def extensions(self):
        return ExtensionsDiscovery(self.config)

    @property
    def imports(self):
        return ImportsDiscovery(self.config)

    @property
    def line_items(self):
        return LineItemsDiscovery(self.config)

    @property
    def objects(self):
        return ObjectsDiscovery(self.config)

    @property
    def pipelines(self):
        return PipelinesDiscovery(self.config)

    @property
    def products(self):
        return ProductsDiscovery(self.config)

    @property
    def properties(self):
        return PropertiesDiscovery(self.config)

    @property
    def quotes(self):
        return QuotesDiscovery(self.config)

    @property
    def owners(self):
        return OwnersDiscovery(self.config)

    @property
    def schemas(self):
        return SchemasDiscovery(self.config)

    @property
    def tickets(self):
        return TicketsDiscovery(self.config)

    @property
    def timeline(self):
        return TimelineDiscovery(self.config)
