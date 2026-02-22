"""
Topic: Functional Programming Patterns.

Using map, filter, and reduce with lambdas to process collections.
"""

from functools import reduce

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    
    # 1. Filter: Keep only even numbers
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(f"Evens: {evens}")
    
    # 2. Map: Double all numbers
    doubled = list(map(lambda x: x * 2, nums))
    print(f"Doubled: {doubled}")
    
    # 3. Reduce: Sum all numbers
    total = reduce(lambda acc, x: acc + x, nums)
    print(f"Sum: {total}")
