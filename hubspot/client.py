from urllib3.util.retry import Retry

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
        from .discovery.auth.discovery import Discovery as AuthDiscovery
        return AuthDiscovery(self.config)

    @property
    def automation(self):
        from .discovery.automation.discovery import Discovery as AutomationDiscovery
        return AutomationDiscovery(self.config)

    @property
    def cms(self):
        from .discovery.cms.discovery import Discovery as CmsDiscovery
        return CmsDiscovery(self.config)

    @property
    def communication_preferences(self):
        from .discovery.communication_preferences.discovery import Discovery as CommunicationPreferencesDiscovery
        return CommunicationPreferencesDiscovery(self.config)

    @property
    def conversations(self):
        from .discovery.conversations.discovery import Discovery as ConversationsDiscovery
        return ConversationsDiscovery(self.config)

    @property
    def crm(self):
        from .discovery.crm.discovery import Discovery as CrmDiscovery
        return CrmDiscovery(self.config)

    @property
    def events(self):
        from .discovery.events.discovery import Discovery as EventsDiscovery
        return EventsDiscovery(self.config)

    @property
    def files(self):
        from .discovery.files.discovery import Discovery as FilesDiscovery
        return FilesDiscovery(self.config)

    @property
    def marketing(self):
        from .discovery.marketing.discovery import Discovery as MarketingDiscovery
        return MarketingDiscovery(self.config)

    @property
    def settings(self):
        from .discovery.settings.discovery import Discovery as SettingsDiscovery
        return SettingsDiscovery(self.config)

    @property
    def webhooks(self):
        from .discovery.webhooks.discovery import Discovery as WebhooksDiscovery
        return WebhooksDiscovery(self.config)
