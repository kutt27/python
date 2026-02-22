"""
Topic: Centralizing business rules (Calculations and Formatting).

DRY Principle: Business logic like discounts or currency formatting 
should be in one place to ensure consistency across the app.
"""

def calculate_discount(amount: float, discount_percent: float) -> float:
    """Calculates discounted amount."""
    discount = amount * (discount_percent / 100)
    return amount - discount

def format_currency(amount: float, currency: str = "USD") -> str:
    """Formats amount as currency string."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "INR": "₹"}
    symbol = symbols.get(currency, "$")
    return f"{symbol}{amount:,.2f}"

# Example Usage:
if __name__ == "__main__":
    amount = 100.00
    discount = 15
    
    final_price = calculate_discount(amount, discount)
    print(f"Price: {format_currency(amount)}")
    print(f"Discount: {discount}%")
    print(f"Final Price: {format_currency(final_price)}")
