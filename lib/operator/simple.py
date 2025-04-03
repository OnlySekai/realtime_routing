def wrap_filter(handler):
    wrapped_handler = lambda x: x if handler(x) is True else None
    wrapped_handler.__name__ = f"filter: \n{getattr(handler, '__name__', str(handler))}"
    return wrapped_handler


def wrap_filter_re(handler):
    wrapped_handler = lambda x: x if handler(x) is False else None
    wrapped_handler.__name__ = f"filter not: \n{getattr(handler, '__name__', str(handler))}"
    return wrapped_handler
