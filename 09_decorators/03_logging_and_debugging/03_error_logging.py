"""
Topic: Centralized Error Logging.

A decorator that wraps code in a try/except block to 
automatically log errors and then re-raise them.
"""

from functools import wraps
import logging

def log_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Replace with real logging in production
            print(f"❌ ERROR in {func.__name__}: {str(e)}")
            raise
    return wrapper

@log_errors
def risky_calc(val):
    return val / 0 # Intentional error

if __name__ == "__main__":
    try:
        risky_calc(10)
    except ZeroDivisionError:
        pass
