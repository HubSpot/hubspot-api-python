from .discovery.discovery import Discovery


class Client:
    @staticmethod
    def create(api_key=None, access_token=None):
        return Discovery({
            'api_key': api_key,
            'access_token': access_token,
        })
