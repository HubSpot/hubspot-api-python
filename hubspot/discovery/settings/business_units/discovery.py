import hubspot.settings.business_units as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def business_unit_api(self) -> api_client.BusinessUnitApi:
        return self._configure_api_client(api_client, "BusinessUnitApi")
