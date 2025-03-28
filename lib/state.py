from lib.event_bus import EventBus


class State(EventBus):
    def __init__(self, parent: 'State' = None):
        self.tempListeners = []
        self.parent = parent
        self.running = False
        super().__init__()

    def bind(self, *handlers):
        """ Thêm các hàm xử lý dữ liệu vào event bus """
        self.tempListeners.extend(handlers)
        return self
    
    def chain_handler(self, *handlers):
        def wrapper(data):
            rs = data
            for h in handlers:
                rs = h(rs)
                if rs is None:
                    return None
            return rs
        return wrapper
    
    def checkpoint(self):
        """ Tạo một event bus mới và chuyển dữ liệu sang đó """
        new_bus = EventBus()
        self.bind(new_bus.emit)
        chained_handler = self.chain_handler(*self.tempListeners)
        super().bind(chained_handler)
        self.tempListeners.clear()
        return new_bus
    
    def getRoot(self):
        if (self.parent is None):
            return self
        return self.parent.getRoot()
    
    def run(self):
        if (self.running):
            return
        self.getRoot().run()
