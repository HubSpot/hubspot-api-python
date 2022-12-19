import hubspot.automation.actions as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def callbacks_api(self) -> api_client.CallbacksApi:
        return self._configure_api_client(api_client, "CallbacksApi")

    @property
    def definitions_api(self) -> api_client.DefinitionsApi:
        return self._configure_api_client(api_client, "DefinitionsApi")

    @property
    def functions_api(self) -> api_client.FunctionsApi:
        return self._configure_api_client(api_client, "FunctionsApi")

    @property
    def revisions_api(self) -> api_client.RevisionsApi:
        return self._configure_api_client(api_client, "RevisionsApi")
