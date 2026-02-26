"""
Topic: Basic Call Logging.

A classic decorator for logging every function call with 
its name and timestamp.
"""

from functools import wraps
from datetime import datetime

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"[{ts}] ⚡ Executing: {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper

@log_call
def place_order(order_id):
    pass

if __name__ == "__main__":
    place_order("ORD-123")
