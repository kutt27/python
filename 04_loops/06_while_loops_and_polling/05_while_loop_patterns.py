"""
Basic While Loop Patterns.
"""

def demonstrate_while_patterns() -> None:
    """
    Demonstrates common while loop patterns.
    """
    print("\nPattern 1: Counter-based")
    counter = 0
    while counter < 3:
        print(f"  Iteration {counter + 1}")
        counter += 1
    
    print("\nPattern 2: Condition-based")
    threshold = 100
    value = 0
    while value < threshold:
        value += 25
        print(f"  Value: {value}")


if __name__ == "__main__":
    demonstrate_while_patterns()
