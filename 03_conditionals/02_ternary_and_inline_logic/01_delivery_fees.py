"""
Delivery Fee Calculator logic.
"""

def calculate_delivery_fee(order_amount: float, customer_tier: str = "standard") -> float:
    """
    Calculates delivery fee based on order amount and customer tier.
    
    Ternary operator provides concise conditional logic:
    value_if_true if condition else value_if_false
    
    Args:
        order_amount: Total order amount
        customer_tier: Customer membership tier
    
    Returns:
        Delivery fee amount
    
    Real-world use case: E-commerce checkout, logistics pricing.
    """
    # Free delivery threshold varies by tier
    free_threshold = 100 if customer_tier == "premium" else 200
    
    # Ternary operator for delivery fee calculation
    delivery_fee = 0 if order_amount >= free_threshold else 9.99
    
    return delivery_fee


def demonstrate_delivery_fees() -> None:
    """
    Demonstrates ternary operator usage for delivery fee calculation.
    
    Real-world use case: E-commerce logistics.
    """
    test_orders = [
        (50, "standard"),
        (150, "standard"),
        (50, "premium"),
        (150, "premium"),
    ]
    
    for amount, tier in test_orders:
        fee = calculate_delivery_fee(amount, tier)
        status = "FREE" if fee == 0 else f"${fee:.2f}"
        print(f"${amount:>6.2f} | {tier:8} tier | Delivery: {status}")


if __name__ == "__main__":
    demonstrate_delivery_fees()
