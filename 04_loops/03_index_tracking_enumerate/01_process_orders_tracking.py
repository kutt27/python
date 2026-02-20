"""
Processing Orders with tracking.
"""

from typing import List

def process_orders_with_tracking(orders: List[str]) -> None:
    """
    Processes orders with position tracking.
    
    Args:
        orders: List of order IDs
    
    Real-world use case: Order processing with progress tracking.
    """
    total = len(orders)
    print(f"\nProcessing {total} orders")
    print("-" * 60)
    
    for index, order_id in enumerate(orders, start=1):
        progress = (index / total) * 100
        print(f"[{index}/{total}] ({progress:.0f}%) Processing order: {order_id}")


def demonstrate_order_tracking() -> None:
    """
    Demonstrates order processing with progress tracking.
    """
    orders = ["ORD-101", "ORD-102", "ORD-103", "ORD-104", "ORD-105"]
    process_orders_with_tracking(orders)


if __name__ == "__main__":
    demonstrate_order_tracking()
