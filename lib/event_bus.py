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