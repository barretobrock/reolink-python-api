from typing import Callable
from threading import Thread


def threaded(fn) -> Callable:
    def wrapper(*args, **kwargs) -> Thread:
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread

    return wrapper
