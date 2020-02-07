from .discovery.discovery import Discovery


class Client:
    @staticmethod
    def create():
        return Discovery()
