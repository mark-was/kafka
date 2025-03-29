from confluent_kafka import Consumer, TopicPartition

BROKER = '127.0.0.1:9092'
TOPIC = 'events'

consumer = Consumer({'bootstrap.servers':BROKER, 'group.id':'events_group', 'enable.auto.commit':False, 'auto.offset.reset':'earliest'})

partition = TopicPartition(TOPIC, 0)
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
    