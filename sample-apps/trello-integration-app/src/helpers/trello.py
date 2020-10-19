import os
from trello import TrelloClient
from repositories import SettingsRepository


def get_auth_url(
    key: str,
    return_url: str,
    name="HubSpot",
    expiration="30days",
    scope="read",
    response_type="token",
):
    return "https://trello.com/1/authorize?key={}&name={}&expiration={}&response_type={}&scope={}&return_url={}".format(
        key, name, expiration, response_type, scope, return_url
    )


def save_token(token):
    SettingsRepository.save_trello_token(token)
    return token


def is_authorized():
    settings = SettingsRepository.find_one()
    return settings.trello_token is not None


def get_token():
    settings = SettingsRepository.find_one()
    return settings.trello_token


def get_client():
    return TrelloClient(
        api_key=os.getenv("TRELLO_API_KEY"),
        token=get_token(),
    )


def search_cards(query=None):
    client = get_client()
    if query is not None and len(query) > 0:
        return client.search(query=query, partial_match=True, models=["cards"])
    else:
        return []


def create_webhook(callback_url, card_id, description=None):
    client = get_client()
    # standard webhook creation method is not correct
    # prepare data manually
    data = {
        "callbackURL": callback_url,
        "idModel": card_id,
        "description": description,
        "key": os.getenv("TRELLO_API_KEY"),
    }
    url = "https://trello.com/1/tokens/{}/webhooks/".format(get_token())
    response = client.http_service.post(
        url, data=data, auth=client.oauth, proxies=client.proxies
    )
    return response.json()


def update_webhook(webhook_id, callback_url):
    client = get_client()
    data = {
        "callbackURL": callback_url,
        "active": "true",
    }
    url = "https://trello.com/1/webhooks/{}".format(webhook_id)
    response = client.http_service.put(
        url, data=data, auth=client.oauth, proxies=client.proxies
    )
    return response.json()
