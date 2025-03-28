from lib.event_bus import EventBus


class State(EventBus):
    def __init__(self, parent: 'State' = None):
        self.parent = parent
        self.running = False
        super().__init__()

    def bind(self, *handlers):
        """ Thêm các hàm xử lý dữ liệu vào event bus """
        self.listeners.extend(self.chainHandler(handlers))
        return self
    
    def chainHandler(self, *handlers):
        def wrapper(data):
            rs = data
            for h in handlers:
                rs = h(rs)
                if rs is None:
                    return None
            return rs
        return wrapper
    
    def getRoot(self):
        if (self.parent is None):
            return self
        return self.parent.getRoot()
    
    def run(self):
        if (self.running):
            return
        self.getRoot().run()
