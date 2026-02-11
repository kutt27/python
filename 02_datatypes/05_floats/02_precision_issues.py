"""
Demonstrates why 0.1 + 0.2 != 0.3 in floating-point arithmetic.
"""

def demonstrate_precision_issues() -> None:
    # The classic float precision error
    result = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result}")
    print(f"Precise representation: {result:.20f}")
    print(f"Equal to 0.3? {result == 0.3}")
    
    # Financial calculation error with floats
    price = 0.1
    quantity = 3
    total = price * quantity
    print(f"\nPrice: 0.1, Quantity: 3, Total: {total}")
    print(f"Is total == 0.3? {total == 0.3}")
    
    # Correct way to compare: using tolerance
    tolerance = 1e-9
    print(f"Comparing with tolerance (1e-9): {abs(total - 0.3) < tolerance}")

if __name__ == "__main__":
    demonstrate_precision_issues()
