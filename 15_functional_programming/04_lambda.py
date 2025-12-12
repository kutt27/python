"""
Functional Python: Lambda Functions
====================================

Topic: Anonymous Functions

Concept:
Small, anonymous functions defined inline.
Syntax: lambda arguments: expression

Real-World Usage:
- Sorting keys
- Short callbacks
- Inline operations for map/filter
"""

from typing import List, Dict

def main():
    print("="*70)
    print("LAMBDA FUNCTIONS".center(70))
    print("="*70)
    
    # 1. Basic Syntax
    # equivalent to: def add(x, y): return x + y
    add = lambda x, y: x + y
    print(f"[1] Basic: 5 + 3 = {add(5, 3)}")
    
    # 2. Usage in Sorting (Key)
    print("\n[2] Sorting Complex Data")
    users = [
        {"name": "Charlie", "age": 35},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
    ]
    
    # Sort by Name
    sorted_name = sorted(users, key=lambda u: u["name"])
    print(f"By Name: {[u['name'] for u in sorted_name]}")
    
    # Sort by Age
    sorted_age = sorted(users, key=lambda u: u["age"])
    print(f"By Age:  {[u['name'] for u in sorted_age]}")
    
    # 3. Usage with Map/Filter
    print("\n[3] Inline with HOFs")
    nums = [1, 2, 3, 4, 5, 6]
    
    # Squares of even numbers
    # Filter evens -> Map square
    evens = filter(lambda x: x % 2 == 0, nums)
    squared_evens = map(lambda x: x**2, evens)
    
    print(f"Squared Evens: {list(squared_evens)}")
    
    # 4. IIFE (Immediately Invoked Function Expression) - Rare in Python but possible
    print("\n[4] Immediate Invocation")
    result = (lambda x: x * 2)(10)
    print(f"Result: {result}")
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Use Lambdas for short, throwaway functions")
    print("• Limited to a SINGLE expression (no multiple statements)")
    print("• Perfect for 'key=' arguments in sort/max/min")
    print("• Don't overuse: If it's complex, write a named function!")
    print("="*70)


if __name__ == "__main__":
    main()
