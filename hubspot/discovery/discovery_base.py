class DiscoveryBase:
    def __init__(self, config):
        self.config = config

    def _configure_api_client(self, api_client, api_name):
        configuration = api_client.Configuration()
        if self.config["api_key"] is not None:
            configuration.api_key['hapikey'] = self.config["api_key"]
        if self.config["access_token"] is not None:
            configuration.access_token = self.config["access_token"]

        return getattr(api_client, api_name)(api_client.ApiClient(configuration))
