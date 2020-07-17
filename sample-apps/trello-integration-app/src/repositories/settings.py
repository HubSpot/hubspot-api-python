from services.db import session, Settings, transactional


class SettingsRepository:
    @classmethod
    @transactional
    def find_one(cls):
        settings = session.query(Settings).first()
        if settings is None:
            settings = Settings()
            session.add(settings)

        return settings

    @classmethod
    @transactional
    def save(cls, settings):
        session.add(settings)
        return settings

    @classmethod
    def save_tokens(cls, access_token, refresh_token, expires_in, expires_at):
        settings = cls.find_one()
        settings.access_token = access_token
        settings.refresh_token = refresh_token
        settings.token_expires_in = expires_in
        settings.token_expires_at = expires_at

        return cls.save(settings)

    @classmethod
    def save_extension_card_id(cls, extension_card_id):
        settings = cls.find_one()
        settings.extension_card_id = extension_card_id

        return cls.save(settings)

    @classmethod
    def save_trello_token(cls, trello_token):
        settings = cls.find_one()
        settings.trello_token = trello_token

        return cls.save(settings)
