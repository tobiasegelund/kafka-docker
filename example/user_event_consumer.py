import json
from kafka import KafkaConsumer

TOPIC_NAME = 'events_topic'

consumer = KafkaConsumer(
    TOPIC_NAME,
    auto_offset_reset='earliest', # where to start reading the messages at
    group_id='event-collector-group-1', # consumer group id
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) # we deserialize our data from json
)

def consume_events():
    for m in consumer:
        # any custom logic you need
        print(m.value)

if __name__ == '__main__':
    consume_events()
