"""
Demonstrates the difference between identity (is) and equality (==).
"""

def demonstrate_identity_vs_equality() -> None:
    # Small integers are cached by Python (interning)
    a = 100
    b = 100
    print(f"a = {a}, b = {b}")
    print(f"a == b: {a == b}  (same value)")
    print(f"a is b: {a is b}  (same object - Python caches small integers)")
    
    # Larger integers are not cached
    x = 1000000
    y = 1000000
    print(f"\nx = {x}, y = {y}")
    print(f"x == y: {x == y}  (same value)")
    print(f"x is y: {x is y}  (different objects)")
    
    print("\nBest Practice: Use '==' for value comparison")
    print("               Use 'is' only for None, True, False, singletons")

if __name__ == "__main__":
    demonstrate_identity_vs_equality()
