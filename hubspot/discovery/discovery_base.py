import pkg_resources


class DiscoveryBase:
    def __init__(self, config):
        self.config = config

    def _configure_api_client(self, api_client_package, api_name):
        configuration = api_client_package.Configuration()
        config = {k: v for k, v in self.config.items() if v is not None}
        if "api_key" in config:
            configuration.api_key["hapikey"] = config["api_key"]
        if "access_token" in config:
            configuration.access_token = config["access_token"]
        if "retry" in config:
            configuration.retries = config["retry"]

        api_client = api_client_package.ApiClient(configuration=configuration)

        package_version = pkg_resources.require("hubspot-api-client")[0].version
        api_client.user_agent = "hubspot-api-client-python; {0}".format(package_version)

        return getattr(api_client_package, api_name)(api_client=api_client)
