from urllib3.util.retry import Retry
from .discovery.discovery import Discovery


class Client:
    @staticmethod
    def create(
        api_key: str = None,
        access_token: str = None,
        retries: Retry = None,
        **kwargs
    ) -> Discovery:
        kwargs['api_key'] = api_key
        kwargs['access_token'] = access_token
        kwargs['retries'] = retries
        return Discovery(kwargs)
