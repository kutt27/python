"""
Topic: Stacking Multiple Decorators.

When you stack decorators, they are applied from bottom to top. 
The top-most decorator is the first one to be called.
"""

from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def get_text():
    return "Hello World"

if __name__ == "__main__":
    # Expect: <b><i>Hello World</i></b>
    print(get_text())
