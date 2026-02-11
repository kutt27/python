# """
# Demonstrates the difference between identity (is) and equality (==).
# """

# def demonstrate_identity_vs_equality() -> None:
#     # Small integers are cached by Python (interning)
#     a = 100
#     b = 100
#     print(f"a = {a}, b = {b}")
#     print(f"a == b: {a == b}  (same value)")
#     print(f"a is b: {a is b}  (same object - Python caches small integers)")
    
#     # Larger integers are not cached
#     x = 100000000
#     y = 100000000
#     print(f"\nx = {x}, y = {y}")
#     print(f"x == y: {x == y}  (same value)")
#     print(f"x is y: {x is y}  (different objects)")
    
#     print("\nBest Practice: Use '==' for value comparison")
#     print("               Use 'is' only for None, True, False, singletons")

# if __name__ == "__main__":
#     demonstrate_identity_vs_equality()


def demonstrate_identity_vs_equality() -> None:
    print("=== Small integers (always cached) ===")
    base = 10
    a = base * 10
    b = base * 10
    print(f"a = {a}, b = {b}")
    print(f"a == b: {a == b}  (same value)")
    print(f"a is b: {a is b}  (same object - Python caches -5 to 256)")
    
    print("\n=== Large integers (separate objects) ===")
    # Use runtime-assigned variables to defeat ALL optimizations
    base = 1000000
    x = base * 10000      # Runtime multiplication
    y = base * 10000      # Same computation, but new object each time
    
    print(f"x = {x}, y = {y}")
    print(f"x == y: {x == y}  (same value)")
    print(f"x is y: {x is y}  (different objects)")
    print(f"id(x): {id(x)}, id(y): {id(y)}")  # Different memory addresses
    
    print("\n=== Best Practice ===")
    print("Use '==' for value comparison")
    print("Use 'is' only for None, True, False, singletons")
    
    # For some reasons I couldn't understand or troubleshoot, I can't clariy why cpython is caching large values
    # when using it directly. Got false when forcing it to create a new object. Which comes to yield the expected
    # behaviour.

if __name__ == "__main__":
    demonstrate_identity_vs_equality()
