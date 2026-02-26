"""
Topic: Preserving Metadata with `functools.wraps`.

When you wrap a function with a decorator, the meta-information 
(like `__name__` and `__doc__`) is lost unless you use the 
`@wraps` decorator inside your wrapper.
"""

from functools import wraps

def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def good_decorator(func):
    @wraps(func) # Copies metadata from 'func' to 'wrapper'
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def say_hi():
    """Tells the user hi."""
    print("Hi!")

@good_decorator
def say_bye():
    """Tells the user bye."""
    print("Bye!")

if __name__ == "__main__":
    print(f"Bad:  {say_hi.__name__} (Doc: {say_hi.__doc__})")
    print(f"Good: {say_bye.__name__} (Doc: {say_bye.__doc__})")
