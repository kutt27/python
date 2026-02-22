"""
Topic: Higher-Order Functions.

Functions that either take other functions as arguments 
or return them.
"""

from typing import Callable

def apply_operation(val: int, func: Callable):
    """Takes a function as an argument."""
    return func(val)

def create_multiplier(factor: int):
    """Returns a function."""
    return lambda x: x * factor

if __name__ == "__main__":
    # Passing a function
    print(f"Apply double: {apply_operation(5, lambda x: x * 2)}")
    
    # Getting a function back
    triple = create_multiplier(3)
    print(f"Triple 10: {triple(10)}")
