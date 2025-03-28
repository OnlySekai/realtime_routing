import threading
from lib.state.state import State
from repositories.kafka.connection import KafkaConfluentConsumerUtiles


class KafkaSink(State):
    def __init__(self, config):
        super().__init__()
        self.consumer_evt = KafkaConfluentConsumerUtiles(config)
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
            with self.lock:
                message = self.consumer.poll(1)
                self.emit(message)
