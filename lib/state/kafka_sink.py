import json
import threading
from lib.state.state import State
from repositories.kafka.connection import KafkaConfluentConsumerUtiles
from confluent_kafka import KafkaException, KafkaError

class KafkaSink(State):
    def __init__(self, topic, config,num_partitions=3):
        super().__init__()
        self.consumer_evt = KafkaConfluentConsumerUtiles(topic, config,num_partitions)
        self.consumer = self.consumer_evt.consumer
        self.lock = threading.Lock()

    def run(self):
        self.lock.acquire()
        if self.running:
            self.lock.release()
            return
        print("Consumer Event Tracking started!")
        self.running = True
        self.lock.release()
        while True:
            message = self.consumer.poll(1.0)
            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    print('%% %s [%d] reached end at offset %d\n' % (message.topic(), message.partition(), message.offset()))
                elif message.error():
                    raise KafkaException(message.error())
            else:
                event = message.value().decode('utf-8')
                event = json.loads(event)
                self.emit(event)
