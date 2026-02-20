"""
Order Validation logic.
"""

from typing import List, Dict

def filter_valid_orders(orders: List[Dict]) -> List[Dict]:
    """
    Filters list to keep only valid orders.
    
    Args:
        orders: List of order dictionaries
    
    Returns:
        List of valid orders
    
    Real-world use case: Data validation, order processing.
    """
    valid_orders = []
    
    print(f"\nFiltering {len(orders)} orders")
    print("-" * 60)
    
    for order in orders:
        order_id = order.get("id")
        amount = order.get("amount", 0)
        status = order.get("status")
        
        # Validation rules
        is_valid = (
            amount > 0 and
            status in ["pending", "processing", "completed"] and
            order_id is not None
        )
        
        if is_valid:
            valid_orders.append(order)
            print(f"  ✓ Order {order_id}: ${amount:.2f} ({status})")
        else:
            print(f"  ✗ Order {order_id}: INVALID")
    
    return valid_orders


def demonstrate_order_validation() -> None:
    """
    Demonstrates conditional filtering during iteration.
    
    Real-world use case: Business rule validation.
    """
    orders = [
        {"id": "ORD-001", "amount": 99.99, "status": "completed"},
        {"id": "ORD-002", "amount": 0, "status": "pending"},  # Invalid: zero amount
        {"id": "ORD-003", "amount": 49.99, "status": "cancelled"},  # Invalid: cancelled status
        {"id": "ORD-004", "amount": 149.99, "status": "processing"},
    ]
    
    valid = filter_valid_orders(orders)
    print(f"\n{len(valid)}/{len(orders)} orders are valid")


if __name__ == "__main__":
    demonstrate_order_validation()
