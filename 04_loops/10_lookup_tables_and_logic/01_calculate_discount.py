"""
Calculate Discount using Dictionaries.
"""

from typing import Dict, Tuple

# Discount types: (percentage_discount, fixed_discount_amount)
DISCOUNT_TIERS: Dict[str, Tuple[float, float]] = {
    "VIP20": (0.20, 0),        # 20% percentage discount
    "FIXED50": (0, 50),        # $50 fixed discount
    "COMBO": (0.10, 25),       # 10% + $25
    "NEWUSER15": (0.15, 0),    # 15% for new users
    "BULK": (0.25, 0),         # 25% bulk discount
}

def calculate_discount(order_total: float, coupon_code: str) -> float:
    """
    Calculates  discount amount based on coupon code.
    
    Args:
        order_total: Order subtotal
        coupon_code: Discount coupon code
    
    Returns:
        Discount amount
    
    Real-world use case: E-commerce checkout, promotional pricing.
    """
    # Get discount values, default to no discount if code invalid
    percent_off, fixed_off = DISCOUNT_TIERS.get(coupon_code, (0, 0))
    
    # Calculate total discount
    discount = (order_total * percent_off) + fixed_off
    
    return min(discount, order_total)  # Can't discount more than order total


def process_orders_with_discounts(orders: list) -> None:
    """
    Processes orders and applies discount codes.
    """
    print("\nProcessing Orders with Discount Codes")
    print("="*70)
    print(f"{'Order ID':10} | {'Total':>8} | {'Coupon':10} | {'Discount':>10} | {'Final':>10}")
    print("-" * 70)
    
    total_revenue = 0
    total_discounts = 0
    
    for order in orders:
        order_id = order['id']
        subtotal = order['total']
        coupon = order.get('coupon', 'NONE')
        
        # Calculate discount using dictionary lookup
        discount = calculate_discount(subtotal, coupon)
        final_amount = subtotal - discount
        
        # Track totals
        total_revenue += final_amount
        total_discounts += discount
        
        print(f"{order_id:10} | ${subtotal:7.2f} | {coupon:10} | ${discount:>9.2f} | ${final_amount:>9.2f}")
    
    print("-" * 70)
    print(f"{'TOTALS':10} | {' ':8} | {' ':10} | ${total_discounts:>9.2f} | ${total_revenue:>9.2f}")


def demonstrate_discounts() -> None:
    """
    Demonstrates discount calculation.
    """
    customer_orders = [
        {"id": "ORD-001", "total": 100.00, "coupon": "VIP20"},
        {"id": "ORD-002", "total": 250.00, "coupon": "FIXED50"},
        {"id": "ORD-003", "total": 150.00, "coupon": "COMBO"},
        {"id": "ORD-004", "total": 75.00, "coupon": "INVALID"},  # Invalid coupon
        {"id": "ORD-005", "total": 500.00, "coupon": "BULK"},
    ]
    
    process_orders_with_discounts(customer_orders)


if __name__ == "__main__":
    demonstrate_discounts()
