import random
import threading
from time import sleep
from lib.state.state import State


class SampleSink(State):
    def __init__(
        self,
        name: str = None,
        des: str = None,
        log: bool = False,
        parent: "State" = None,
    ):
        super().__init__(parent=parent, name=name, des=des, log=log)
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
            sleep(2)
            self.emit(random.randint(0, 100))
