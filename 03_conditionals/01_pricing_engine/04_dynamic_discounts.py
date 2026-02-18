"""
Dynamic Discount Calculator logic.
"""

from typing import Optional

def determine_discount(order_total: float, customer_type: str, promo_code: Optional[str] = None) -> float:
    """
    Determines discount percentage based on multiple conditions.
    
    Args:
        order_total: Order subtotal
        customer_type: Type of customer (new/returning/vip)
        promo_code: Optional promo code
    
    Returns:
        Discount percentage (0-100)
    
    Real-world use case: Promotional pricing, customer loyalty programs.
    """
    discount = 0.0
    
    # Base discount by customer type
    if customer_type == "vip":
        discount = 15.0
    elif customer_type == "returning":
        discount = 5.0
    elif customer_type == "new":
        discount = 10.0  # New customer incentive
    
    # Additional discount for large orders
    if order_total > 200:
        discount += 5.0
    elif order_total > 100:
        discount += 2.5
    
    # Promo code overrides (if better)
    if promo_code == "SAVE20":
        discount = max(discount, 20.0)
    elif promo_code == "FLASH30":
        discount = max(discount, 30.0)
    
    # Cap at 40%
    return min(discount, 40.0)


def demonstrate_dynamic_discounts() -> None:
    """
    Demonstrates complex discount logic with multiple conditions.
    
    Real-world use case: Promotional engines.
    """
    test_scenarios = [
        (50, "new", None),
        (150, "returning", None),
        (250, "vip", None),
        (80, "new", "SAVE20"),
        (300, "vip", "FLASH30"),
    ]
    
    for total, cust_type, promo in test_scenarios:
        discount = determine_discount(total, cust_type, promo)
        final_price = total * (1 - discount / 100)
        
        promo_str = f"+ {promo}" if promo else ""
        print(f"${total:>6.2f} | {cust_type:9} {promo_str:10} | {discount:>5.1f}% off | Final: ${final_price:.2f}")


if __name__ == "__main__":
    demonstrate_dynamic_discounts()
