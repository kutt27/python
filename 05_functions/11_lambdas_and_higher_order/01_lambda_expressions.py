"""
Topic: Lambda Expressions (Anonymous Functions).

Small, one-line functions that can be created on the fly. 
Commonly used for short-lived logic in sorting or mapping.
"""

if __name__ == "__main__":
    # Lambda for squaring numbers
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda as a sort key
    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    # Sort by age (the second element of the tuple)
    sorted_data = sorted(data, key=lambda x: x[1])
    print(f"Sorted by age: {sorted_data}")
