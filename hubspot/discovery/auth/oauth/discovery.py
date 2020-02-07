import hubspot.codegen.auth.oauth as oauth
import hubspot.codegen.auth.oauth.exceptions as exceptions
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    def default_api(self):
        configuration = oauth.Configuration()
        configuration.api_key = self.config["api_key"]
        configuration.access_token = self.config["access_token"]

        return oauth.DefaultApi(oauth.ApiClient(configuration))

    def exceptions(self):
        return exceptions
