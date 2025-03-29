import json
import random
import time
from confluent_kafka import Producer

BROKER = "127.0.0.1:9092"
TOPIC = "events"

producer = Producer({'bootstrap.servers':BROKER})

def make_event():
    event_type = random.choice(["login", "logout", "purchase"])
    event_data = {
        "timestamp": int(time.time()),
        "type": event_type,
        "data": {
            "username": f"user{random.randint(1, 1000)}"
        }
    }
    return json.dumps(event_data)


while True:
    event = make_event()
    producer.produce(TOPIC, key=None, value=event)
    time.sleep(random.uniform(0, 1))
    producer.flush()
    print(f"Sent event: {event}")
    time.sleep(1)