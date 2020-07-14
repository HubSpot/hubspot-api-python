from services.db import session, Association


def is_deal_associated(deal_id):
    count = session.query(Association).filter_by(deal_id=deal_id).count()
    session.commit()

    return count > 0


def find_association_by_deal_id(deal_id):
    association = session.query(Association).filter_by(deal_id=deal_id).first()
    session.commit()

    return association


def find_associations_by_card_id(card_id):
    associations = session.query(Association).filter_by(card_id=card_id).all()
    session.commit()

    return associations


def create_association(deal_id, card_id):
    association = Association()
    association.deal_id = deal_id
    association.card_id = card_id
    session.add(association)
    session.commit()

    return association


def delete_association_by_deal_id(deal_id):
    session.query(Association).filter_by(deal_id=deal_id).delete()
    session.commit()
