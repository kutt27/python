"""
Functional Python: Functools Utilities
=======================================

Topic: functools.partial and functools.reduce

Concept:
- Partial Application: Pre-filling arguments to create a specialized function.
"""

from functools import partial
from typing import Callable

def power(base: int, exponent: int) -> int:
    return base ** exponent

def log_message(level: str, source: str, msg: str):
    print(f"[{level.upper()}] {source}: {msg}")

def main():
    print("="*70)
    print("FUNCTOOLS & PARTIAL APPLICATION".center(70))
    print("="*70)
    
    print("\n[1] Partial Application (Power)")
    # Create new functions processing specific logic from general ones
    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)
    
    print(f"Square(5): {square(5)}") # Internally calls power(5, exponent=2)
    print(f"Cube(5):   {cube(5)}")
    
    print("\n[2] Partial Application (Logging)")
    # Create specialized loggers
    info_log = partial(log_message, level="info", source="MainModule")
    error_log = partial(log_message, level="error", source="MainModule")
    
    info_log(msg="Application started")
    error_log(msg="Connection failed")
    
    print("\n[3] Replacing Lambdas")
    # Instead of: map(lambda x: power(x, 2), data)
    data = [1, 2, 3, 4]
    squared = list(map(partial(power, exponent=2), data))
    print(f"Squared Map: {squared}")
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• `partial` freezes specific arguments of a function")
    print("• Creates specialized reusable functions")
    print("• Often cleaner than lambda functions")
    print("="*70)


if __name__ == "__main__":
    main()
