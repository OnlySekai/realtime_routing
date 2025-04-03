"""
This module provides simple operator wrappers for filtering data.
"""
def wrap_filter(handler):
    """
    Wraps a filter handler to return the input if the handler returns True, otherwise returns None.

    Args:
        handler: The filter handler function.

    Returns:
        The wrapped handler function.
    """
    wrapped_handler = lambda x: x if handler(x) is True else None
    wrapped_handler.__name__ = f"filter: \n{getattr(handler, '__name__', str(handler))}"
    return wrapped_handler


def wrap_filter_re(handler):
    """
    Wraps a filter handler to return the input if the handler returns False, otherwise returns None.

    Args:
        handler: The filter handler function.

    Returns:
        The wrapped handler function.
    """
    wrapped_handler = lambda x: x if handler(x) is False else None
    wrapped_handler.__name__ = f"filter not: \n{getattr(handler, '__name__', str(handler))}"
    return wrapped_handler
