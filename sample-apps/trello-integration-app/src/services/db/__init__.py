from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import *


_engine = create_engine(getenv("DB_URL"))
_Session = sessionmaker(bind=_engine)
session = _Session()


def create_db_schema():
    Base.metadata.create_all(
        _engine,
        tables=[
            Settings.__table__,
            Association.__table__,
            Mapping.__table__,
        ]
    )
