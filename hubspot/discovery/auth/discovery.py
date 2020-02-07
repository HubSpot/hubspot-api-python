from .oauth.discovery import Discovery as OAuthDiscovery


class Discovery:
    def oauth(self):
        return OAuthDiscovery()
