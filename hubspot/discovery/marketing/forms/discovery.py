import hubspot.marketing.forms as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def forms_api(self) -> api_client.FormsApi:
        return self._configure_api_client(api_client, "FormsApi")