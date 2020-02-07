from .auth.discovery import Discovery as AuthDiscovery


class Discovery:
    def auth(self):
        return AuthDiscovery()
