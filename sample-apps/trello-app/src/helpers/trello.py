from services.redis import redis

TOKEN_KEY = "trello_token"


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
