def wrap_filter(handler):
    return lambda x: x if handler(x) is True else None

def wrap_filter_re(handler):
    return lambda x: x if handler(x) is False else None
