from services.db import session, Mapping, transactional


class MappingsRepository:
    @classmethod
    @transactional
    def save(cls, mapping):
        session.add(mapping)
        return mapping

    @classmethod
    @transactional
    def find_by(cls, **kwargs):
        return session.query(Mapping).filter_by(**kwargs).all()

    @classmethod
    @transactional
    def get(cls, mapping_id):
        return session.query(Mapping).get(mapping_id)

    @classmethod
    @transactional
    def delete_by_id(cls, mapping_id):
        session.delete(session.query(Mapping).get(mapping_id))
