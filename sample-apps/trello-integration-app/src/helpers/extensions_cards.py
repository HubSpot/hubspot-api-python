from repositories.settings import find_settings, save_extension_card_id

CARD_ID_KEY = "extension_card_id"
CARD_TITLE = "Trello Integration Test Card"


def get_card_id():
    settings = find_settings()
    return settings.extension_card_id


def save_card_id(card_id):
    return save_extension_card_id(card_id)
