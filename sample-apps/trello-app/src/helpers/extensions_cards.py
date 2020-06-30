from services.redis import redis

CARD_ID_KEY = "extension_card_id"
CARD_TITLE = "Trello Integration Test Card"

def get_card_id():
    if redis.exists(CARD_ID_KEY):
        return redis.get(CARD_ID_KEY).decode()
    return None


def save_card_id(card_id):
    return redis.set(CARD_ID_KEY, card_id)
