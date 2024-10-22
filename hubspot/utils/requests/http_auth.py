class Auth:
    @staticmethod
    def get_auth_types() -> list:
        return ["accessToken", "developerApiKey", "hapikey"]

    @staticmethod
    def _has_auth_value(source: dict) -> bool:
        return bool(source.get("auth_value"))

    @staticmethod
    def choose_auth(options: dict, config: dict) -> dict:
        auth_types = Auth.get_auth_types()
        auth_type = options.get("auth_type")

        if auth_type in auth_types and Auth._has_auth_value(options):
            return {
                "auth_type": auth_type,
                "auth_value": options["auth_value"]
            }

        config_auth_type = config.get("auth_type")
        if config_auth_type in auth_types and Auth._has_auth_value(config):
            return {
                "auth_type": config_auth_type,
                "auth_value": config["auth_value"]
            }

        return {
            "auth_type": None,
            "auth_value": None
        }

