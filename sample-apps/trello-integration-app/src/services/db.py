import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    DateTime,
    VARCHAR,
    func,
)
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.getenv("DB_URL"))
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Association(Base):
    __tablename__ = "associations"

    id = Column(Integer, primary_key=True)

    deal_id = Column(VARCHAR(length=255))
    card_id = Column(VARCHAR(length=255))

    created_at = Column(DateTime, default=func.now())


class Mapping(Base):
    __tablename__ = "mappings"

    id = Column(Integer, primary_key=True)

    board_id = Column(VARCHAR(length=255))
    board_list_id = Column(VARCHAR(length=255))

    pipeline_id = Column(VARCHAR(length=255))
    pipeline_stage_id = Column(VARCHAR(length=255))

    created_at = Column(DateTime, default=func.now())


def create_db_schema():
    Base.metadata.create_all(engine, tables=[Association.__table__, Mapping.__table__])
