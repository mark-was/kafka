import argparse
from confluent_kafka import Consumer, TopicPartition

BROKER = '127.0.0.1:9092'
TOPIC = 'events'
PARTITION = 0

#argparses
parser = argparse.ArgumentParser(description='Consume events from Kafka')
parser.add_argument('-p', '--partition', help='partition to consume from', default=PARTITION)
parser.add_argument('-t', '--topic', help='topic to consume from', default=TOPIC)
args = parser.parse_args()

PARTITION = int(args.partition)
TOPIC = args.topic

consumer = Consumer({'bootstrap.servers':BROKER, 'group.id':'events_group', 'enable.auto.commit':False, 'auto.offset.reset':'earliest'})


partition = TopicPartition(TOPIC, PARTITION)

consumer.assign([partition])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(f'Error: {msg.error()}')
        continue

    print(f'Received message: {msg.value().decode("utf-8")}')
    consumer.commit()