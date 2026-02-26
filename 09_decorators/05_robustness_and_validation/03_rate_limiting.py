"""
Topic: Simple Rate Limiting.

A decorator that restricts how frequently a function can be executed. 
This is helpful for throttling API requests or expensive tasks.
"""

from functools import wraps
import time

def throttle(seconds):
    """Prevents a function from being called too frequently."""
    last_called = 0
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            elapsed = time.time() - last_called
            
            if elapsed < seconds:
                wait_time = seconds - elapsed
                print(f"🛑 Throttled! Wait {wait_time:.2f}s more.")
                return None
                
            last_called = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@throttle(seconds=2)
def send_email(to):
    print(f"📧 Email sent to {to}")

if __name__ == "__main__":
    send_email("alice@example.com") # Success
    send_email("bob@example.com")   # Throttled
    
    print("Waiting 2 seconds...")
    time.sleep(2.1)
    send_email("charlie@example.com") # Success
