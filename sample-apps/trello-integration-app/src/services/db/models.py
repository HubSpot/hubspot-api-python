from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    VARCHAR,
    func,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True)

    access_token = Column(VARCHAR(length=255))
    refresh_token = Column(VARCHAR(length=255))
    token_expires_in = Column(Integer)
    token_expires_at = Column(DateTime)

    extension_card_id = Column(VARCHAR(length=255))
    trello_token = Column(VARCHAR(length=255))

    created_at = Column(DateTime, default=func.now())


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

    __table_args__ = (
        UniqueConstraint("board_id", "board_list_id", "pipeline_id", name="_unique_1"),
        UniqueConstraint(
            "pipeline_id", "pipeline_stage_id", "board_id", name="_unique_2"
        ),
    )


class Webhook(Base):
    __tablename__ = "webhooks"

    webhook_id = Column(VARCHAR(length=255), primary_key=True)
    card_id = Column(VARCHAR(length=255))
    url = Column(VARCHAR(length=255))

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __table_args__ = (UniqueConstraint("card_id", name="_unique_1"),)
