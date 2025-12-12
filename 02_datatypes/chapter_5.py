"""
Python Floating-Point Numbers and Precision
============================================

Topic: Float data type, precision issues, and alternatives (Decimal, Fraction)

Real-World Applications:
- Financial calculations and currency handling
- Scientific computing and measurements
- ML model hyperparameters and metrics
- Sensor data processing in IoT systems
"""

import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from typing import Union


def demonstrate_float_basics() -> None:
    """
    Demonstrates basic floating-point operations and precision.
    
    Real-world use case: Temperature monitoring in server infrastructure.
    """
    # Example: Server temperature monitoring
    target_temp_celsius = 65.5
    current_temp_celsius = 65.49
    
    temperature_diff = target_temp_celsius - current_temp_celsius
    
    print(f"Target temperature: {target_temp_celsius}°C")
    print(f"Current temperature: {current_temp_celsius}°C")
    print(f"Temperature difference: {temperature_diff}°C")
    
    # Check if within acceptable range
    tolerance = 0.5
    is_within_range = abs(temperature_diff) <= tolerance
    print(f"\nWithin acceptable range (±{tolerance}°C): {is_within_range}")


def demonstrate_float_precision_issues() -> None:
    """
    Demonstrates floating-point precision limitations.
    
    WARNING: Floats have limited precision due to binary representation.
    This can cause unexpected results in calculations.
    
    Real-world impact: Financial calculations, scientific computing, comparisons.
    """
    print(f"\n{'='*60}")
    print("FLOATING-POINT PRECISION ISSUES")
    print(f"{'='*60}")
    
    # Classic example: 0.1 + 0.2 != 0.3
    result = 0.1 + 0.2
    print(f"\n0.1 + 0.2 = {result}")
    print(f"Expected: 0.3")
    print(f"Actual: {result:.20f}")
    print(f"Equal to 0.3? {result == 0.3}")
    
    # Example: Cumulative error in financial calculations
    price = 0.1  # $0.10
    quantity = 3
    total = price * quantity
    
    print(f"\nPrice: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total}")
    print(f"Precise representation: ${total:.20f}")
    
    # The RIGHT way to compare floats
    expected = 0.3
    tolerance = 1e-9
    is_close = abs(total - expected) < tolerance
    print(f"\nComparing with tolerance {tolerance}: {is_close}")


def demonstrate_decimal_precision() -> None:
    """
    Demonstrates Decimal type for exact decimal arithmetic.
    
    Use Decimal for:
    - Financial calculations (money, prices, taxes)
    - Situations requiring exact decimal representation
    - When precision is critical
    
    Real-world use case: E-commerce pricing and tax calculations.
    """
    print(f"\n{'='*60}")
    print("DECIMAL TYPE: EXACT PRECISION")
    print(f"{'='*60}")
    
    # Set precision for Decimal operations
    getcontext().prec = 10
    
    # Example: E-commerce price calculation
    item_price = Decimal('19.99')
    tax_rate = Decimal('0.08')  # 8% sales tax
    quantity = 3
    
    subtotal = item_price * quantity
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    
    print(f"\nItem price: ${item_price}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax ({tax_rate * 100}%): ${tax_amount}")
    print(f"Total: ${total}")
    
    # Round to 2 decimal places for currency
    total_rounded = total.quantize(Decimal('0.01'))
    print(f"Total (rounded): ${total_rounded}")
    
    print(f"\n{'='*60}")
    print("IMPORTANT: Always use string literals with Decimal")
    print("  ✓ Correct: Decimal('0.1')")
    print("  ✗ Wrong:   Decimal(0.1)  <- Inherits float imprecision")
    print(f"{'='*60}")


def demonstrate_fraction() -> None:
    """
    Demonstrates Fraction type for exact rational number representations.
    
    Use Fraction for:
    - Mathematical calculations requiring exact ratios
    - Converting between different units
    - When you need exact fractional representations
    
    Real-world use case: Recipe scaling, unit conversions.
    """
    print(f"\n{'='*60}")
    print("FRACTION TYPE: EXACT RATIOS")
    print(f"{'='*60}")
    
    # Example: API rate limiting - requests per second
    requests_allowed = 100
    time_window_seconds = 60
    
    rate_per_second = Fraction(requests_allowed, time_window_seconds)
    print(f"\nRate limiting:")
    print(f"  {requests_allowed} requests per {time_window_seconds} seconds")
    print(f"  Rate: {rate_per_second} requests/second")
    print(f"  Decimal: {float(rate_per_second):.4f} requests/second")
    
    # Example: Dividend among microservices
    total_load = 1000
    services = 3
    
    load_per_service = Fraction(total_load, services)
    print(f"\nLoad distribution:")
    print(f"  Total load: {total_load} req/sec")
    print(f"  Services: {services}")
    print(f"  Load per service: {load_per_service}")
    print(f"  Decimal: {float(load_per_service):.2f} req/sec")


def demonstrate_float_info() -> None:
    """
    Demonstrates Python's float implementation details.
    
    Useful for understanding:
    - Float range and limits
    - Precision capabilities
    - Platform-specific behavior
    """
    print(f"\n{'='*60}")
    print("FLOAT IMPLEMENTATION DETAILS (sys.float_info)")
    print(f"{'='*60}")
    
    print(f"\nMaximum float value: {sys.float_info.max}")
    print(f"Minimum positive float: {sys.float_info.min}")
    print(f"Decimal digits of precision: {sys.float_info.dig}")
    print(f"Mantissa digits: {sys.float_info.mant_dig}")
    print(f"Epsilon (smallest difference): {sys.float_info.epsilon}")
    print(f"Radix (base): {sys.float_info.radix}")


def calculate_compound_interest(
    principal: Decimal,
    rate: Decimal,
    time_years: int
) -> Decimal:
    """
    Calculates compound interest using Decimal for precision.
    
    Args:
        principal: Initial investment amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time_years: Number of years
    
    Returns:
        Final amount after compound interest
    
    Real-world use case: Financial applications requiring exact calculations.
    """
    # A = P(1 + r)^t
    multiplier = (Decimal('1') + rate) ** time_years
    final_amount = principal * multiplier
    
    return final_amount.quantize(Decimal('0.01'))


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON FLOATING-POINT NUMBERS & PRECISION".center(70))
    print("="*70)
    
    print("\n[1] FLOAT BASICS")
    print("-" * 70)
    demonstrate_float_basics()
    
    print("\n\n[2] PRECISION ISSUES")
    print("-" * 70)
    demonstrate_float_precision_issues()
    
    print("\n\n[3] DECIMAL FOR EXACT ARITHMETIC")
    print("-" * 70)
    demonstrate_decimal_precision()
    
    print("\n\n[4] FRACTION FOR EXACT RATIOS")
    print("-" * 70)
    demonstrate_fraction()
    
    print("\n\n[5] FLOAT IMPLEMENTATION INFO")
    print("-" * 70)
    demonstrate_float_info()
    
    print("\n\n[6] PRACTICAL EXAMPLE: Compound Interest")
    print("-" * 70)
    principal = Decimal('10000.00')
    rate = Decimal('0.05')  # 5% annual rate
    years = 10
    
    final_amount = calculate_compound_interest(principal, rate, years)
    interest_earned = final_amount - principal
    
    print(f"Principal: ${principal}")
    print(f"Rate: {rate * 100}% per year")
    print(f"Time: {years} years")
    print(f"Final amount: ${final_amount}")
    print(f"Interest earned: ${interest_earned}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Floats have limited precision - avoid for financial calculations")
    print("2. Use Decimal for exact decimal arithmetic (money, taxes)")
    print("3. Use Fraction for exact rational numbers (ratios, rates)")
    print("4. Always compare floats with tolerance, never with ==")
    print("5. Initialize Decimal with strings: Decimal('0.1'), not Decimal(0.1)")
    print("="*70)


if __name__ == "__main__":
    main()