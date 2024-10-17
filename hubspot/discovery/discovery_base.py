try:
    import importlib.metadata as metadata
except ImportError:
    import importlib_metadata as metadata


class DiscoveryBase:
    def __init__(self, config):
        self.config = config

    def _configure_api_client(self, api_client_package, api_name):
        api_factory = self.config.get("api_factory") or self._default_api_factory
        config = {k: v for k, v in self.config.items() if k != "api_factory" and v is not None}
        return api_factory(api_client_package, api_name, config)

    @staticmethod
    def _default_api_factory(api_client_package, api_name, config):
        configuration = api_client_package.Configuration()
        for key in config:
            if key == "api_key":
                configuration.api_key["developer_hapikey"] = config["api_key"]
            elif key == "retry":
                configuration.retries = config["retry"]
            else:
                setattr(configuration, key, config[key])

        api_client = api_client_package.ApiClient(configuration=configuration)
        package_version = metadata.version("hubspot-api-client")
        api_client.user_agent = "hubspot-api-client-python; {0}".format(package_version)

        return getattr(api_client_package, api_name)(api_client=api_client)
