from services.db import session, Association


class AssociationsRepository:
    @classmethod
    def is_deal_associated(cls, deal_id):
        count = session.query(Association).filter_by(deal_id=deal_id).count()
        session.commit()

        return count > 0

    @classmethod
    def find_one_by_deal_id(cls, deal_id):
        association = session.query(Association).filter_by(deal_id=deal_id).first()
        session.commit()

        return association

    @classmethod
    def find_by_card_id(cls, card_id):
        associations = session.query(Association).filter_by(card_id=card_id).all()
        session.commit()

        return associations

    @classmethod
    def create(cls, deal_id, card_id):
        association = Association()
        association.deal_id = deal_id
        association.card_id = card_id
        session.add(association)
        session.commit()

        return association

    @classmethod
    def delete_by_deal_id(cls, deal_id):
        session.query(Association).filter_by(deal_id=deal_id).delete()
        session.commit()
