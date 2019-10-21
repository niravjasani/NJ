from contextlib import contextmanager
from threading import Timer
import threading
import time
import sys

class TimeoutException(Exception):
    pass

@contextmanager
def time_limit(seconds):
    def default_handler():
        raise TimeoutException('Timed out!')
    timer = threading.Timer(seconds, default_handler)
    timer.start() 
    # time.sleep(6)
    
    try:
        yield
    finally:
        timer.cancel()

with time_limit(3):
    print("Hello World")
