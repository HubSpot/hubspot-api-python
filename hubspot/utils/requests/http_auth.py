class Auth:
    @staticmethod
    def get_auth_types() -> list:
        return ["access_token", "api_key"]

    @staticmethod
    def _has_auth_value(source: dict, key: str) -> bool:
        return bool(source.get(key))

    @staticmethod
    def choose_auth(config: dict, options: dict) -> dict:
        auth_types = Auth.get_auth_types()
        auth_type = options.get("auth_type")

        if auth_type in auth_types and Auth._has_auth_value(config, auth_type):
            return {"auth_type": auth_type}

        else:
            for key in auth_types:
                if key in config and Auth._has_auth_value(config, key):
                    return {"auth_type": key}

        return {"auth_type": None}

