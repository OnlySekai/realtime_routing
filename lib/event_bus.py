class EventBus:
    def __init__(self):
        self.listeners = []

    def bind(self, *handlers):
        """ Thêm các hàm xử lý dữ liệu vào event bus """
        self.listeners.extend(handlers)
        return self

    def emit(self, data):
        if data is None:
            return
        """ Gửi dữ liệu đến tất cả các listeners """
        for listener in self.listeners:
            listener(data)

    def checkpoint(self):
        """ Tạo một event bus mới và chuyển dữ liệu sang đó """
        new_bus = EventBus()
        self.bind(new_bus.emit)
        return new_bus