"""
Range Variations logic.
"""

def demonstrate_range_variations() -> None:
    """
    Demonstrates the various parameters of the range() function.
    
    Real-world use case: Flexible loop control.
    """
    # Basic range
    print("range(5):", list(range(5)))
    
    # Start and stop
    print("range(1, 6):", list(range(1, 6)))
    
    # With step
    print("range(0, 10, 2):", list(range(0, 10, 2)))
    
    # Reverse
    print("range(10, 0, -1):", list(range(10, 0, -1)))


if __name__ == "__main__":
    demonstrate_range_variations()
