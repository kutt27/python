"""
Topic: Basic List Comprehensions (Transformations).

List comprehensions provide a concise way to create lists by 
transforming elements from an existing iterable.
"""

def demonstrate_transformations():
    numbers = [1, 2, 3, 4, 5]
    
    # 1. Square each number
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")
    
    # 2. Convert to strings
    strings = [f"Item-{x}" for x in numbers]
    print(f"Strings: {strings}")
    
    # 3. Currency conversion
    prices_usd = [10.0, 25.5, 100.0]
    prices_eur = [p * 0.92 for p in prices_usd]
    print(f"Prices (EUR): {prices_eur}")

if __name__ == "__main__":
    demonstrate_transformations()
