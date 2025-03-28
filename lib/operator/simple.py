def wrap_filter(handler):
    return lambda x: x if handler(x) is True else None
