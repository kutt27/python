"""
Functional Python: Pure Functions
==================================

Topic: Pure Functions & Referential Transparency

Concept:
A pure function has two key properties:
1. It always produces the same output for the same arguments.
2. It has no side effects (doesn't modify external state, I/O, etc.).

Real-World Benefits:
- Easier to test (no mocking needed)
- Cacheable (Memoization)
- Thread-safe (Parallelization)
"""

import datetime
from typing import List, Dict

# --- IMPURE FUNCTIONS (Avoid where possible) ---

# Global state
_cart_total = 0

def add_to_cart_impure(price: float):
    """Impure: Modifies global state."""
    global _cart_total
    _cart_total += price
    return _cart_total

def get_time_impure():
    """Impure: Different output every time (depends on system time)."""
    return datetime.datetime.now()

def log_data_impure(message: str):
    """Impure: IO operation (Side effect)."""
    print(f"[LOG] {message}")


# --- PURE FUNCTIONS (Preferred) ---

def calculate_new_total(current_total: float, price: float) -> float:
    """
    Pure: Output depends ONLY on inputs.
    No side effects.
    """
    return current_total + price

def format_greeting(time_of_day: str, name: str) -> str:
    """Pure: String formatting."""
    return f"Good {time_of_day}, {name}!"

def update_inventory(inventory: Dict[str, int], item: str, qty: int) -> Dict[str, int]:
    """
    Pure: Returns a NEW dictionary instead of modifying the input.
    (Simulates immutability)
    """
    # Create copy
    new_inventory = inventory.copy()
    current_qty = new_inventory.get(item, 0)
    new_inventory[item] = current_qty + qty
    return new_inventory


def main():
    print("="*70)
    print("PURE vs IMPURE FUNCTIONS".center(70))
    print("="*70)
    
    # Impure Usage
    print("\n[1] Impure Approaches")
    print(f"Initial Global Total: {_cart_total}")
    add_to_cart_impure(50)
    print(f"Modified Global Total: {_cart_total}")
    
    # Pure Usage
    print("\n[2] Pure Approaches")
    initial_inv = {"apple": 10, "banana": 5}
    print(f"Original Inventory: {initial_inv}")
    
    # Returns new state, originals untouched
    new_inv = update_inventory(initial_inv, "apple", -2)
    
    print(f"New Inventory:      {new_inv}")
    print(f"Original Inventory: {initial_inv} (Unchanged!)")
    
    print(f"\n[3] Purity enables Caching")
    # If calculate_new_total is pure, calculate_new_total(100, 50) is ALWAYS 150.
    # We can cache this result safely.
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Strive for Pure Functions in business logic")
    print("• Push 'Impure' code (I/O, DB, Global State) to the boundaries")
    print("• Makes core logic testable and predictable")
    print("="*70)


if __name__ == "__main__":
    main()
