"""
Topic: Simple Memoization (Caching).

A decorator that caches function results for unique arguments 
to avoid re-executing expensive recursive calls.
"""

from functools import wraps

def memoize(func):
    """Simple cache for function results."""
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib(n):
    """Recursive Fibonacci - much faster with memoization."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    import time
    start = time.time()
    result = fib(35)
    print(f"Result: {result} (Time: {time.time() - start:.4f}s)")
