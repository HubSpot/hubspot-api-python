from services.redis import redis


def _format_deal_association_key(deal_id):
    return "deal_association_{}".format(deal_id)


def is_deal_associated(deal_id):
    return redis.exists(_format_deal_association_key(deal_id))


def get_deal_association(deal_id):
    return redis.get(_format_deal_association_key(deal_id)).decode()


def associate_deal(deal_id, card_id):
    redis.set(_format_deal_association_key(deal_id), card_id)


def remove_deal_association(deal_id):
    redis.delete(_format_deal_association_key(deal_id))
