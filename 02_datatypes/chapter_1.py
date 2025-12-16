"""
Python Variables and Object Identity
=====================================

Topic: Understanding Python's object model, name binding, and identity vs equality

Real-World Applications:
- Configuration management in production systems
- Memory optimization for large-scale data processing
- Understanding reference behavior in ML tensor operations
- Debugging object mutation issues in concurrent applications
"""

from typing import Any

def demonstrate_memory_address() -> None:
    """
    Demonstrates how to check object memory addresses.
    
    The id() function returns the memory address of an object.
    This is useful for:
    - Debugging reference issues
    - Understanding object lifecycle
    - Verifying immutability
    - Profiling memory usage
    """
    # Configuration example: Database connection strings
    db_host_dev = "localhost"
    db_host_prod = "db.production.com"
    
    print(f"\nDevelopment DB: {db_host_dev}")
    print(f"Memory ID: {id(db_host_dev)}")
    print(f"Hex address: {hex(id(db_host_dev))}")
    
    print(f"\nProduction DB: {db_host_prod}")
    print(f"Memory ID: {id(db_host_prod)}")
    print(f"Hex address: {hex(id(db_host_prod))}")
    
    # String interning for identical strings
    db_host_dev2 = "localhost"
    print(f"\nString interning demo:")
    print(f"db_host_dev is db_host_dev2: {db_host_dev is db_host_dev2}")
    print("Python interns(caches) short strings for memory efficiency")


def demonstrate_name_binding() -> None:
    """
    Demonstrates Python's name binding mechanism.
    
    In Python, variables are names that reference objects in memory.
    When you reassign a variable, you're changing what object it points to,
    not mutating the original object (for immutable types).
    
    Real-world use case: Understanding this prevents bugs in configuration
    management where you expect value changes to affect all references.
    """
    # Example: API rate limit configuration
    max_requests = 100  # Initial rate limit
    print(f"Initial rate limit: {max_requests}")
    print(f"Memory address of 100: {id(max_requests)}")
    
    # Changing configuration
    max_requests = 1000  # New rate limit for premium users
    print(f"\nUpdated rate limit: {max_requests}")
    print(f"Memory address of 1000: {id(max_requests)}")
    
    # Key insight: The name 'max_requests' now points to a different object
    # The integer 100 still exists in memory, but 'max_requests' no longer references it
    print(f"\n{'='*60}")
    print("IMPORTANT: Integer objects are IMMUTABLE")
    print("Reassignment changes the REFERENCE, not the VALUE")
    print(f"{'='*60}")


def demonstrate_identity_vs_equality() -> None:
    """
    Demonstrates the difference between identity (is) and equality (==).
    
    - 'is' checks if two names reference the SAME object (identity)
    - '==' checks if two objects have the SAME value (equality)
    
    Real-world use case: Singleton pattern validation, None checking,
    debugging unexpected behavior in caching systems.
    """
    # Small integers are cached by Python (interning)
    a = 100
    b = 100
    print(f"\na = {a}, b = {b}")
    print(f"a == b: {a == b}  (same value)")
    print(f"a is b: {a is b}  (same object - Python caches small integers)")
    print(f"id(a): {id(a)}, id(b): {id(b)}")
    
    # Larger integers are not cached
    x = 1000000
    y = 1000000
    print(f"\nx = {x}, y = {y}")
    print(f"x == y: {x == y}  (same value)")
    print(f"x is y: {x is y}  (different objects)")
    print(f"id(x): {id(x)}, id(y): {id(y)}")
    

    print(f"\n{'='*60}")
    print("Best Practice: Use '==' for value comparison")
    print("               Use 'is' only for None, True, False, singletons")
    print(f"{'='*60}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON OBJECT MODEL: NAME BINDING & IDENTITY".center(70))
    print("="*70)
    
    print("\n[1] NAME BINDING DEMONSTRATION")
    print("-" * 70)
    demonstrate_name_binding()
    
    print("\n\n[2] IDENTITY VS EQUALITY")
    print("-" * 70)
    demonstrate_identity_vs_equality()
    
    print("\n\n[3] MEMORY ADDRESSES")
    print("-" * 70)
    demonstrate_memory_address()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Variables are names that reference objects")
    print("2. Immutable objects (int, str, tuple) create new objects on 'change'")
    print("3. Use '==' for value comparison, 'is' for identity checks")
    print("4. Python optimizes memory by caching small integers and strings")
    print("="*70)


if __name__ == "__main__":
    main()