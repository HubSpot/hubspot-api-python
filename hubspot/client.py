from urllib3.util.retry import Retry
from .discovery.auth.discovery import Discovery as AuthDiscovery
from .discovery.automation.discovery import Discovery as AutomationDiscovery
from .discovery.crm.discovery import Discovery as CrmDiscovery
from .discovery.cms.discovery import Discovery as CmsDiscovery
from .discovery.webhooks.discovery import Discovery as WebhooksDiscovery


class Client:
    def __init__(
        self,
        api_key: str = None,
        access_token: str = None,
        retry: Retry = None,
        **kwargs
    ):
        self.config = dict(
            {"api_key": api_key, "access_token": access_token, "retry": retry}, **kwargs
        )

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)

    @property
    def access_token(self):
        return self.config["access_token"]

    @access_token.setter
    def access_token(self, value):
        self.config["access_token"] = value

    @property
    def api_key(self):
        return self.config["api_key"]

    @api_key.setter
    def api_key(self, value):
        self.config["api_key"] = value

    @property
    def auth(self):
        return AuthDiscovery(self.config)

    @property
    def automation(self):
        return AutomationDiscovery(self.config)

    @property
    def cms(self):
        return CmsDiscovery(self.config)

    @property
    def crm(self):
        return CrmDiscovery(self.config)

    @property
    def webhooks(self):
        return WebhooksDiscovery(self.config)
