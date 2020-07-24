from services.db import session, Webhook, transactional


class WebhooksRepository:
    @classmethod
    @transactional
    def get(cls, webhooks_id):
        return session.query(Webhook).get(webhooks_id)

    @classmethod
    @transactional
    def save(cls, webhook):
        session.add(webhook)
        return webhook

    @classmethod
    @transactional
    def create(cls, webhook_id, card_id, url):
        webhook = Webhook()
        webhook.webhook_id = webhook_id
        webhook.card_id = card_id
        webhook.url = url
        session.add(webhook)
        return webhook

    @classmethod
    @transactional
    def find_by(cls, **kwargs):
        return session.query(Webhook).filter_by(**kwargs).all()

    @classmethod
    @transactional
    def find_outdated(cls, url):
        print(url, flush=True)
        return session.query(Webhook).filter(Webhook.url != url).all()
