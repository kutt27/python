"""
Demonstrates truthiness - which values evaluate to True or False in a boolean context.
"""

def demonstrate_truthiness() -> None:
    # Falsy values
    print("Falsy values:")
    print(f"  bool(0): {bool(0)}")
    print(f"  bool(''): {bool('')}")
    print(f"  bool([]): {bool([])}")
    print(f"  bool(None): {bool(None)}")
    
    # Truthy values
    print("\nTruthy values:")
    print(f"  bool(5): {bool(5)}")
    print(f"  bool('admin'): {bool('admin')}")
    print(f"  bool([1, 2]): {bool([1, 2])}")

if __name__ == "__main__":
    demonstrate_truthiness()
