from services.kafka import get_consumer

consumer = get_consumer()
for message in consumer:
    message = message.value
    print(message)
