"""
Demonstrates Decimal for exact arithmetic, ideal for financial calculations.
"""

from decimal import Decimal, getcontext

def demonstrate_decimal() -> None:
    # Set context precision
    getcontext().prec = 10
    
    # Use strings to initialize Decimals
    price = Decimal('19.99')
    tax_rate = Decimal('0.08')
    quantity = 3
    
    total = price * quantity * (1 + tax_rate)
    print(f"Price: {price}, Tax: {tax_rate}, Quantity: {quantity}")
    print(f"Total: {total}")
    
    # Quantize for currency formatting
    print(f"Total (rounded): {total.quantize(Decimal('0.01'))}")
    
    print("\nIMPORTANT: Always initialize Decimal with strings: Decimal('0.1')")

if __name__ == "__main__":
    demonstrate_decimal()
