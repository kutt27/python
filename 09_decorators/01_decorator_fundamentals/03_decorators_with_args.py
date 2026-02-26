"""
Topic: Decorators with Arguments.

To pass arguments to a decorator (e.g., '@repeat(3)'), you need 
to create a 'decorator factory'—a function that returns a 
decorator.
"""

from functools import wraps

def repeat(times):
    """Factory that returns a decorator to repeat a function."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")
