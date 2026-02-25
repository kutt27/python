"""
Topic: Using `itertools` for Infinite Iterators.

Python's `itertools` module provides several built-in generators 
for common infinite sequence patterns.
"""

import itertools

if __name__ == "__main__":
    # 1. count(start, step)
    cnt = itertools.count(100, 10)
    print(f"count: {[next(cnt) for _ in range(3)]}")
    
    # 2. cycle(iterable)
    colors = itertools.cycle(["Red", "Green", "Blue"])
    print(f"cycle: {[next(colors) for _ in range(7)]}")
    
    # 3. repeat(object, times)
    echo = itertools.repeat("Hello", 3)
    print(f"repeat: {list(echo)}")
