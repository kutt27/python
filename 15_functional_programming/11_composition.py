"""
Functional Python: Composition
===============================

Topic: Explicit Function Composition

Concept:
Combine two functions f(x) and g(x) into h(x) = f(g(x)).
Python doesn't have a native compose operator (like Haskell's dot), so we build one.
"""

from typing import Callable
from functools import reduce

def compose(*functions: Callable) -> Callable:
    """
    Compose multiple functions right-to-left.
    compose(f, g, h)(x) == f(g(h(x)))
    """
    def compose2(f, g):
        return lambda x: f(g(x))
        
    return reduce(compose2, functions)

# Basic helpers
def double(x: int) -> int: return x * 2
def increment(x: int) -> int: return x + 1
def as_string(x: int) -> str: return f"Value: {x}"

def main():
    print("="*70)
    print("FUNCTION COMPOSITION".center(70))
    print("="*70)
    
    input_val = 5
    
    # 1. Manual Nesting (Hard to read)
    res_manual = as_string(double(increment(input_val)))
    print(f"Manual:   {res_manual}")
    
    # 2. Composition helper
    # Logic: increment -> double -> as_string
    # Passed in reverse order: compose(last, middle, first)
    pipeline = compose(as_string, double, increment)
    
    res_composed = pipeline(input_val)
    print(f"Composed: {res_composed}")
    
    # 3. Dynamic Pipeline
    transformations = [increment, increment, double]
    # We can reduce over a list of functions
    pipe = compose(*reversed(transformations))
    print(f"Dynamic:  {pipe(5)}") # (5+1+1)*2 = 14
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Composition builds complex logic from simple blocks")
    print("• Usually read right-to-left (standard mathematical definition)")
    print("• Allows building dynamic processing chains")
    print("="*70)


if __name__ == "__main__":
    main()
