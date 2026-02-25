"""
Topic: Memory Efficiency (List vs Generator).

Generators compute values on-the-fly, meaning they don't store 
the entire sequence in memory.
"""

import sys

def get_numbers_list(n: int):
    return [i ** 2 for i in range(n)]

def get_numbers_generator(n: int):
    for i in range(n):
        yield i ** 2

if __name__ == "__main__":
    n = 100_000
    
    l = get_numbers_list(n)
    g = get_numbers_generator(n)
    
    print(f"List size:      {sys.getsizeof(l):,} bytes")
    print(f"Generator size: {sys.getsizeof(g):,} bytes")
    print(f"Generators use the same amount of memory regardless of 'n'.")
