from .discovery.discovery import Discovery


class Client:
    @staticmethod
    def create(
        api_key=None,
        access_token=None,
        retries=None,
        **kwargs
    ):
        kwargs['api_key'] = api_key
        kwargs['access_token'] = access_token
        kwargs['retries'] = retries
        return Discovery(kwargs)
