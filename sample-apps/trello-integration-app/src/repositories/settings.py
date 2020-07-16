from services.db import session, Settings


def find_settings():
    settings = session.query(Settings).first()
    if settings is None:
        settings = Settings()
        session.add(settings)
        session.commit()

    return settings


def save_settings(settings):
    session.add(settings)
    session.commit()

    return settings


def save_tokens(access_token, refresh_token, expires_in, expires_at):
    settings = find_settings()
    settings.access_token = access_token
    settings.refresh_token = refresh_token
    settings.expires_in = expires_in
    settings.expires_at = expires_at

    return save_settings(settings)


def save_extension_card_id(extension_card_id):
    settings = find_settings()
    settings.extension_card_id = extension_card_id

    return save_settings(settings)


def save_trello_token(trello_token):
    settings = find_settings()
    settings.trello_token = trello_token

    return save_settings(settings)
