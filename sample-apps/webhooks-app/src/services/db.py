import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    BigInteger,
    DateTime,
    VARCHAR,
    func,
)
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.getenv("DB_URL"))
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    event_type = Column(VARCHAR(length=255))
    object_id = Column(Integer)
    event_id = Column(BigInteger)

    property_name = Column(VARCHAR(length=255))
    property_value = Column(VARCHAR(length=255))

    occurred_at = Column(DateTime)
    created_at = Column(DateTime, default=func.now())


def create_db_schema():
    Base.metadata.create_all(engine, tables=[Event.__table__])
