"""
Topic: Multiple Return Values.

Python can return multiple values as a tuple, which can be 
cleanly unpacked by the caller.
"""

from typing import Tuple

def calculate_cart(items: list) -> Tuple[float, float, float]:
    """Returns (subtotal, tax, total)."""
    subtotal = sum(items)
    tax = subtotal * 0.08
    total = subtotal + tax
    return subtotal, tax, total

if __name__ == "__main__":
    prices = [10.0, 25.0, 15.0]
    
    # Unpaking multiple returns
    sub, tx, tot = calculate_cart(prices)
    
    print(f"Subtotal: ${sub:.2f}")
    print(f"Tax:      ${tx:.2f}")
    print(f"Total:    ${tot:.2f}")
