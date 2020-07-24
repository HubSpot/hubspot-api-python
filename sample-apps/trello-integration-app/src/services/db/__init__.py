from os import getenv
from functools import wraps
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import *

_engine = create_engine(getenv("DB_URL"))
_Session = sessionmaker(bind=_engine)
session = _Session()


def transactional(func_):
    @wraps(func_)
    def inner(*args, **kwargs):
        try:
            result = func_(*args, **kwargs)
            session.commit()
            return result
        except:
            session.rollback()
            raise

    return inner


def create_db_schema():
    Base.metadata.create_all(
        _engine,
        tables=[
            Settings.__table__,
            Association.__table__,
            Mapping.__table__,
            Webhook.__table__,
        ],
    )
