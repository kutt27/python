"""
Shipping Cost Calculator logic.
"""

def calculate_shipping_cost(order_total: float, is_premium: bool = False) -> float:
    """
    Calculates shipping cost with conditional logic.
    
    Args:
        order_total: Order subtotal
        is_premium: Whether customer has premium membership
    
    Returns:
        Shipping cost
    
    Real-world use case: E-commerce checkout, shipping calculations.
    """
    # Ternary operator for concise conditional
    shipping = 0 if (order_total > 50 or is_premium) else 5.99
    
    return shipping


def demonstrate_shipping_costs() -> None:
    """
    Demonstrates shipping cost calculation using ternary operators.
    
    Real-world use case: E-commerce checkout.
    """
    test_orders = [
        (30.00, False, "Regular customer, low order"),
        (75.00, False, "Regular customer, free shipping"),
        (25.00, True, "Premium customer, any order"),
    ]
    
    for total, is_premium, description in test_orders:
        cost = calculate_shipping_cost(total, is_premium)
        status = "FREE" if cost == 0 else f"${cost:.2f}"
        print(f"${total:6.2f} | {'Premium' if is_premium else 'Regular':8} | {status:>8} | {description}")


if __name__ == "__main__":
    demonstrate_shipping_costs()
