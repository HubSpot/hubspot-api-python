import os
import json
from kafka import KafkaProducer, KafkaConsumer

_producer = None
_consumer = None


def get_producer():
    global _producer
    if _producer is None:
        _producer = KafkaProducer(
            bootstrap_servers=os.getenv("KAFKA_BROKER_LIST"),
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )
    return _producer


def get_consumer():
    global _consumer
    if _consumer is None:
        _consumer = KafkaConsumer(
            os.getenv("EVENTS_TOPIC"),
            bootstrap_servers=os.getenv("KAFKA_BROKER_LIST"),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="events-group",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )
    return _consumer
