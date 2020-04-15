from urllib3.util.retry import Retry
from .discovery.auth.discovery import Discovery as AuthDiscovery
from .discovery.crm.discovery import Discovery as CrmDiscovery
from .discovery.webhooks.discovery import Discovery as WebhooksDiscovery


class Client:
    @classmethod
    def create(
        cls,
        api_key: str = None,
        access_token: str = None,
        retry: Retry = None,
        **kwargs
    ):
        config = dict({
            'api_key': api_key,
            'access_token': access_token,
            'retry': retry,
        }, **kwargs)
        return cls(config)

    def __init__(self, config):
        self.config = config

    @property
    def access_token(self):
        return self.config['access_token']

    @access_token.setter
    def access_token(self, value):
        self.config['access_token'] = value

    @property
    def api_key(self):
        return self.config['api_key']

    @api_key.setter
    def api_key(self, value):
        self.config['api_key'] = value

    @property
    def auth(self):
        return AuthDiscovery(self.config)

    @property
    def crm(self):
        return CrmDiscovery(self.config)

    @property
    def webhooks(self):
        return WebhooksDiscovery(self.config)
