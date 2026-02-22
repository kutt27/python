"""
Topic: Execution Tracing with Decorators.

A decorator can be used to automatically log when a function is 
called, what its arguments were, and what it returned.
"""

from functools import wraps

def trace(func):
    """Decorator that prints function entry and exit."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"→ Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} returned {result}")
        return result
    return wrapper

@trace
def add(a, b):
    return a + b

@trace
def greet(name, msg="Hello"):
    return f"{msg}, {name}"

if __name__ == "__main__":
    add(10, 20)
    greet("Alice", msg="Welcome")
