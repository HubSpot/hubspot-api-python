from ..discovery_base import DiscoveryBase

class Discovery(DiscoveryBase):
    @property
    def associations(self):
        from .associations.discovery import Discovery as AssociationsDiscovery
        return AssociationsDiscovery(self.config)

    @property
    def contacts(self):
        from .contacts.discovery import Discovery as ContactsDiscovery
        return ContactsDiscovery(self.config)

    @property
    def companies(self):
        from .companies.discovery import Discovery as CompaniesDiscovery
        return CompaniesDiscovery(self.config)

    @property
    def deals(self):
        from .deals.discovery import Discovery as DealsDiscovery
        return DealsDiscovery(self.config)

    @property
    def extensions(self):
        from .extensions.discovery import Discovery as ExtensionsDiscovery
        return ExtensionsDiscovery(self.config)

    @property
    def imports(self):
        from .imports.discovery import Discovery as ImportsDiscovery
        return ImportsDiscovery(self.config)

    @property
    def line_items(self):
        from .line_items.discovery import Discovery as LineItemsDiscovery
        return LineItemsDiscovery(self.config)

    @property
    def lists(self):
        from .lists.discovery import Discovery as ListsDiscovery
        return ListsDiscovery(self.config)

    @property
    def objects(self):
        from .objects.discovery import Discovery as ObjectsDiscovery
        return ObjectsDiscovery(self.config)

    @property
    def pipelines(self):
        from .pipelines.discovery import Discovery as PipelinesDiscovery
        return PipelinesDiscovery(self.config)

    @property
    def products(self):
        from .products.discovery import Discovery as ProductsDiscovery
        return ProductsDiscovery(self.config)

    @property
    def properties(self):
        from .properties.discovery import Discovery as PropertiesDiscovery
        return PropertiesDiscovery(self.config)

    @property
    def quotes(self):
        from .quotes.discovery import Discovery as QuotesDiscovery
        return QuotesDiscovery(self.config)

    @property
    def owners(self):
        from .owners.discovery import Discovery as OwnersDiscovery
        return OwnersDiscovery(self.config)

    @property
    def schemas(self):
        from .schemas.discovery import Discovery as SchemasDiscovery
        return SchemasDiscovery(self.config)

    @property
    def tickets(self):
        from .tickets.discovery import Discovery as TicketsDiscovery
        return TicketsDiscovery(self.config)

    @property
    def timeline(self):
        from .timeline.discovery import Discovery as TimelineDiscovery
        return TimelineDiscovery(self.config)
