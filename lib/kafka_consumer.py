from lib.state import State
from repositories.kafka.connection import KafkaConfluentConsumerUtiles


class KafkaSink(State):
    def __init__(self, config):
        super().__init__()
        self.consumer_evt = KafkaConfluentConsumerUtiles(config)
        self.consumer = self.consumer_evt.consumer

    def run(self):
        print("Consumer Event Tracking started!")
        while True:
            message = self.consumer.poll(1)
            self.emit(message)