import pkg_resources


class DiscoveryBase:
    def __init__(self, config):
        self.config = config

    def _configure_api_client(self, api_client_package, api_name):
        configuration = api_client_package.Configuration()
        if self.config["api_key"] is not None:
            configuration.api_key['hapikey'] = self.config["api_key"]
        if self.config["access_token"] is not None:
            configuration.access_token = self.config["access_token"]

        api_client = api_client_package.ApiClient(configuration=configuration)

        package_version = pkg_resources.require("hubspot")[0].version
        api_client.user_agent = 'hubspot-api-python; {0}'.format(package_version)

        return getattr(api_client_package, api_name)(api_client=api_client)
