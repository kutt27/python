"""
Regional Tax Calculation.
"""

from typing import Dict

def calculate_regional_tax(amount: float, region_code: str) -> float:
    """
    Calculates tax based on regional tax rates.
    
    Args:
        amount: Order amount
        region_code: Region/state code
    
    Returns:
        Tax amount
    
    Real-world use case: E-commerce tax calculation, compliance.
    """
    TAX_RATES: Dict[str, float] = {
        "CA": 0.0725,  # California: 7.25%
        "NY": 0.0400,  # New York: 4%
        "TX": 0.0625,  # Texas: 6.25%
        "FL": 0.06,    # Florida: 6%
        "WA": 0.065,   # Washington: 6.5%
    }
    
    tax_rate = TAX_RATES.get(region_code, 0)  # Default: no tax
    return amount * tax_rate


def demonstrate_tax() -> None:
    """
    Demonstrates tax calculation.
    """
    order_amount = 100.00
    regions = ["CA", "NY", "TX", "FL", "WA", "UNKNOWN"]
    
    print(f"\nTax calculation for ${order_amount:.2f} order:")
    print(f"{'Region':8} | {'Tax Rate':>10} | {'Tax Amount':>12} | {'Total':>10}")
    print("-" * 50)
    
    for region in regions:
        tax = calculate_regional_tax(order_amount, region)
        tax_rate = (tax / order_amount * 100) if tax > 0 else 0
        total = order_amount + tax
        
        print(f"{region:8} | {tax_rate:>9.2f}% | ${tax:>10.2f} | ${total:>9.2f}")


if __name__ == "__main__":
    demonstrate_tax()
