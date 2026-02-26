"""
Topic: Basic Decorator Syntax.

A decorator is a function that takes another function and extends 
its behavior without explicitly modifying it. The '@' syntax is 
shorthand for 'func = decorator(func)'.
"""

def simple_decorator(func):
    """Wraps a function to print before and after execution."""
    def wrapper():
        print("Decorator: Before the function runs")
        func()
        print("Decorator: After the function runs")
    return wrapper

@simple_decorator
def say_hello():
    print("Function: Hello World!")

if __name__ == "__main__":
    # Call the decorated function
    say_hello()
