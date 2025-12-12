"""
Functional Python: Higher-Order Functions
==========================================

Topic: Functions that take or return other functions

Concept:
In functional programming, functions are "First-Class Citizens".
They can be passed as arguments, returned from functions, and assigned to variables.

Common HOFs: map, filter, reduce
"""

from functools import reduce
from typing import Callable, List, Iterable

# --- 1. Functions as Arguments ---

def apply_operation(numbers: List[int], op: Callable[[int], int]) -> List[int]:
    """Applies a function 'op' to every number in the list."""
    # This is essentially 'map'
    return [op(n) for n in numbers]

def square(x: int) -> int: return x * x
def cube(x: int) -> int: return x * x * x


def main():
    print("="*70)
    print("HIGHER-ORDER FUNCTIONS".center(70))
    print("="*70)
    
    data = [1, 2, 3, 4, 5]
    
    print(f"Data: {data}")
    
    # 1. Custom HOF
    print("\n[1] Custom HOF (apply_operation)")
    sq_res = apply_operation(data, square)
    print(f"Squared: {sq_res}")
    
    cb_res = apply_operation(data, cube)
    print(f"Cubed:   {cb_res}")
    
    # 2. Built-in map()
    print("\n[2] Built-in map()")
    # map returns an iterator, convert to list to view
    map_res = list(map(str, data)) 
    print(f"Stringified: {map_res}")
    
    # 3. Built-in filter()
    print("\n[3] Built-in filter()")
    def is_even(n): return n % 2 == 0
    filter_res = list(filter(is_even, data))
    print(f"Evens only: {filter_res}")
    
    # 4. functools.reduce()
    print("\n[4] functools.reduce()")
    # Accumulates a value across a list
    # ((1+2)+3)+4...
    def add(x, y): return x + y
    
    total = reduce(add, data, 0) # Initial value 0
    print(f"Sum (Reduce): {total}")
    
    product = reduce(lambda x, y: x*y, data, 1) # Initial value 1
    print(f"Product (Reduce): {product}")
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• HOFs abstract away the control flow (loops)")
    print("• `map` transforms data")
    print("• `filter` selects data")
    print("• `reduce` combines data")
    print("="*70)


if __name__ == "__main__":
    main()
