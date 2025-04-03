import threading
import copy

from config import FOR_DRAW



class State:
    def __init__(
        self,
        parent: "State" = None,
        name: str = None,
        des: str = None,
        log: bool = False
    ):
        self.parent = parent
        self.running = False
        self.listeners = []
        self.join_point = []
        self.des = des
        self.name = name
        self.log = log
        self.list_state = []
        self.for_draw = FOR_DRAW
        super().__init__()



    def chain_handler(self, handlers):
        def wrapper(data):
            rs = data
            for h in handlers:
                try:
                    rs = h(rs)
                    if rs is None:
                        return None
                except Exception as e:
                    print(f"Error in handler {h}: {e}")
                    return None
            return rs

        return wrapper

    def bind(self, *handlers):
        """Thêm các hàm xử lý dữ liệu vào event bus"""
        self.listeners.extend(handlers)
        return self

    def emit(self, data):
        if self.log:
            print(f"Event {self.name} receive: {data}")
        chained_handler = self.chain_handler(self.listeners)(data)
        if self.log:
            print(f"Event {self.name} processing: {chained_handler}")
            print("-----------------------------")
        if chained_handler is None:
            return
        for listener in self.join_point:
            threading.Thread(
                target=listener, args=[copy.deepcopy(chained_handler)]
            ).start()

    def fork(self, name: str = None, des: str = None, log: bool = False):
        """Tạo một event bus mới và chuyển dữ liệu sang đó"""
        new_bus = State(parent=self, name=name, des=des, log=log)
        if self.for_draw:
            root = self.getRoot()
            root.list_state.append(new_bus)
        self.join_point.append(new_bus.emit)
        return new_bus

    def getRoot(self):
        if self.parent is None:
            return self
        return self.parent.getRoot()

    def run(self):
        if self.running:
            return
        self.getRoot().run()