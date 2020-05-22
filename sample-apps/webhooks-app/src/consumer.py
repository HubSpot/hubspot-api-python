import datetime
from services.kafka import get_consumer
from services.logger import logger
from services.db import Event, session

consumer = get_consumer()
for message in consumer:
    message = message.value
    logger.info(message)

    event = Event()
    event.event_type = message["subscriptionType"]
    event.event_id = message["eventId"]
    event.object_id = message["objectId"]
    event.occurred_at = datetime.datetime.fromtimestamp(message["occurredAt"] // 1000)
    if "propertyName" in message:
        event.property_name = message["propertyName"]
    if "propertyValue" in message:
        event.property_value = message["propertyValue"]

    session.add(event)
    session.commit()
