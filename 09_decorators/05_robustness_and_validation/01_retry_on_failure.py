"""
Topic: Automatic Retries.

A decorator that catches exceptions and retries the function 
multiple times before giving up. Useful for network requests 
or database connections.
"""

from functools import wraps
import time
import random

def retry(max_attempts=3, delay=0.5):
    """Retries a function if it fails."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == max_attempts:
                        print(f"❌ Effort {i} failed: {e}. No retries left.")
                        raise
                    print(f"⚠️ Effort {i} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1)
def flakey_api():
    if random.random() < 0.7: # 70% chance of failure
        raise ConnectionError("Server Timed Out")
    return "API Success!"

if __name__ == "__main__":
    try:
        print(flakey_api())
    except ConnectionError:
        print("Completed with errors.")
