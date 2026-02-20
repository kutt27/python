"""
Transaction Totals calculation.
"""

from typing import List, Tuple

def calculate_transaction_totals(
    items: List[str],
    quantities: List[int],
    prices: List[float]
) -> List[Tuple[str, int, float, float]]:
    """
    Calculates totals for each transaction item.
    
    Args:
        items: Item names
        quantities: Quantities purchased
        prices: Unit prices
    
    Returns:
        List of (item, quantity, unit_price, total) tuples
    
    Real-world use case: E-commerce cart total calculation.
    """
    transactions = []
    
    for item, qty, price in zip(items, quantities, prices):
        total = qty * price
        transactions.append((item, qty, price, total))
    
    return transactions


def demonstrate_totals() -> None:
    """
    Demonstrates transaction total calculation.
    """
    cart_items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
    quantities = [1, 2, 1, 1]
    unit_prices = [999.99, 29.99, 79.99, 299.99]
    
    transactions = calculate_transaction_totals(cart_items, quantities, unit_prices)
    
    print("\nOrder Summary:")
    print(f"{'Item':12} | {'Qty':>3} | {'Unit Price':>10} | {'Total':>10}")
    print("-" * 50)
    
    grand_total = 0
    for item, qty, price, total in transactions:
        print(f"{item:12} | {qty:>3} | ${price:>9.2f} | ${total:>9.2f}")
        grand_total += total
    
    print("-" * 50)
    print(f"{'GRAND TOTAL':>28} | ${grand_total:>9.2f}")


if __name__ == "__main__":
    demonstrate_totals()
