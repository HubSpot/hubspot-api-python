import hubspot.codegen.auth.oauth as oauth
import hubspot.codegen.auth.oauth.exceptions as exceptions
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    def default_api(self):
        return self._configure_api_client(oauth, 'DefaultApi')

    def exceptions(self):
        return exceptions
