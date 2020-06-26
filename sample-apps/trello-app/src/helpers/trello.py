import os
from trello import TrelloClient
from services.redis import redis

TOKEN_KEY = "trello_token"
SEARCH_QUERY_KEY = "trello_search_query"


def get_auth_url(key: str, return_url: str, name="HubSpot", expiration="30days", scope="read", response_type="token"):
    return "https://trello.com/1/authorize?key={}&name={}&expiration={}&response_type={}&scope={}&return_url={}".format(
        key, name, expiration, response_type, scope, return_url
    )


def save_token(token):
    redis.set(TOKEN_KEY, token)

    return token


def is_authorized():
    return redis.exists(TOKEN_KEY)


def get_token():
    return redis.get(TOKEN_KEY)


def get_client():
    return TrelloClient(
        api_key=os.getenv("TRELLO_API_KEY"),
        token=get_token(),
    )


def search_cards(query=None):
    client = get_client()
    if query is not None and len(query) > 0:
        return client.search(query=query)
    else:
        return []


def get_search_query():
    if redis.exists(SEARCH_QUERY_KEY):
        return redis.get(SEARCH_QUERY_KEY).decode()
    else:
        return os.getenv("TRELLO_DEFAULT_SEARCH_QUERY")


def save_search_query(query):
    redis.set(SEARCH_QUERY_KEY, query)
