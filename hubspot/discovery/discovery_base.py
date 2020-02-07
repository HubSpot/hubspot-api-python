class DiscoveryBase:
    def __init__(self, config):
        self.config = config

    def _configure_api_client(self, client_module, api_name):
        configuration = client_module.Configuration()
        configuration.api_key = self.config["api_key"]
        configuration.access_token = self.config["access_token"]

        return getattr(client_module, api_name)(client_module.ApiClient(configuration))
