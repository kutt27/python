"""
Functional Python: Recursion
=============================

Topic: Recursive functions vs Iteration

Concept:
Solving a problem by breaking it down into smaller instances of the same problem.
Python has a recursion limit (default 1000), so deep recursion needs care.

"""

import sys
from functools import lru_cache
import time

# 1. Standard Recursion (Factorial)
def factorial_rec(n: int) -> int:
    """Basic recursive factorial."""
    if n <= 1: # Base case
        return 1
    return n * factorial_rec(n - 1) # Recursive step

# 2. Tail Recursion Optimization (Simulated)
# Python does NOT support TCO naturally, but this is the concept.
def factorial_tail(n: int, accumulator: int = 1) -> int:
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

# 3. Memoized Recursion (Fibonacci)
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """Recursion with caching."""
    if n < 2:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

def fib_basic(n: int) -> int:
    """Naive recursion (SLOW)."""
    if n < 2:
        return n
    return fib_basic(n-1) + fib_basic(n-2)

def main():
    sys.setrecursionlimit(2000) # Increasing limit slightly
    
    print("="*70)
    print("RECURSION".center(70))
    print("="*70)
    
    print("\n[1] Basic Recursion")
    print(f"5! = {factorial_rec(5)}")
    
    print("\n[2] Memoization Speedup")
    n = 35
    print(f"Calculating Fib({n})...")
    
    start = time.time()
    # print(f"Naive Result: {fib_basic(n)}") # This would take seconds
    print("Naive: Skipped (Too slow)")
    
    start = time.time()
    res = fib_memo(n)
    print(f"Memoized Result: {res}")
    print(f"Memoized Time:   {time.time() - start:.6f}s")
    
    print("\n[3] Handling Hierarchy (Directory Walk Example)")
    fake_fs = {
        "home": {
            "user": {
                "docs": ["resume.pdf", "todo.txt"],
                "pics": ["me.jpg"]
            }
        },
        "etc": ["config.sys"]
    }
    
    def list_files(structure, path=""):
        if isinstance(structure, list):
            for item in structure:
                print(f"File: {path}/{item}")
        elif isinstance(structure, dict):
            for key, val in structure.items():
                list_files(val, f"{path}/{key}")
                
    list_files(fake_fs)
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Recursion is elegant for hierarchical data (Trees, JSON)")
    print("• Use `@lru_cache` for Dynamic Programming problems")
    print("• Beware of RecursionError in Python (use loops for simple linear logic)")
    print("="*70)


if __name__ == "__main__":
    main()
