"""
Topic: Memory Efficiency with Generator Expressions.

Unlike list comprehensions, generator expressions use parentheses `()` 
and compute values one at a time (laizly). This saves a massive 
amount of memory for large datasets.
"""

import sys

def demonstrate_memory():
    n = 1_000_000
    
    # List comprehension (allocates all values in memory!)
    list_comp = [x**2 for x in range(n)]
    
    # Generator expression (computes values only when asked)
    gen_exp = (x**2 for x in range(n))
    
    print(f"List size:      {sys.getsizeof(list_comp):,}")
    print(f"Generator size: {sys.getsizeof(gen_exp):,}")

if __name__ == "__main__":
    demonstrate_memory()
