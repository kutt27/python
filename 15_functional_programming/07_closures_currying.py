"""
Functional Python: Closures & Currying
=======================================

Topic: Closures and Function Factories

Concept:
- Closure: A function that remembers values from its enclosing scope.
- Currying: Transforming f(a, b, c) into f(a)(b)(c).
"""

from typing import Callable

# 1. Closure Example
def make_multiplier(factor: int) -> Callable[[int], int]:
    """Function Factory returns a function."""
    
    def multiplier(n: int) -> int:
        # 'factor' is captured from outer scope
        return n * factor
        
    return multiplier

# 2. Currying Example
def price_calculator(tax_rate: float):
    """
    Curried function:
    Step 1: Set tax rate
    Step 2: Set discount
    Step 3: Calculate price
    """
    def with_discount(discount: float):
        def calculate(base_price: float):
            price_after_discount = base_price * (1 - discount)
            final_price = price_after_discount * (1 + tax_rate)
            return round(final_price, 2)
        return calculate
    return with_discount


def main():
    print("="*70)
    print("CLOSURES & CURRYING".center(70))
    print("="*70)
    
    print("\n[1] Closures (Multipliers)")
    doubler = make_multiplier(2)
    tripler = make_multiplier(3)
    
    print(f"Double 10: {doubler(10)}")
    print(f"Triple 10: {tripler(10)}")
    
    print("\n[2] Currying (Configurable Logic)")
    # Configure for NY State (8.8% tax)
    ny_pricing = price_calculator(0.088)
    
    # Configure different sales events
    black_friday_calc = ny_pricing(0.50) # 50% off
    standard_calc = ny_pricing(0.0)      # 0% off
    
    item_price = 100.0
    print(f"Item Price: ${item_price}")
    print(f"Standard NY Price:    ${standard_calc(item_price)}")
    print(f"Black Friday NY Price: ${black_friday_calc(item_price)}")
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Closures encapsulate state (alternative to Classes)")
    print("• Use factories `make_something()` to configure behavior")
    print("• Currying builds complex functions step-by-step")
    print("="*70)


if __name__ == "__main__":
    main()
