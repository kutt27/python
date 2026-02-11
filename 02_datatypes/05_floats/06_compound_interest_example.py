"""
Calculates compound interest using the Decimal module for financial accuracy.
"""

from decimal import Decimal

def calculate_compound_interest(principal: Decimal, rate: Decimal, years: int) -> Decimal:
    # A = P(1 + r)^t
    amount = principal * ((Decimal('1') + rate) ** years)
    return amount.quantize(Decimal('0.01'))

if __name__ == "__main__":
    p = Decimal('10000.00')
    r = Decimal('0.05')
    y = 10
    
    final = calculate_compound_interest(p, r, y)
    print(f"Principal: ${p}")
    print(f"Rate: {r*100}% for {y} years")
    print(f"Final Amount: ${final}")
    print(f"Interest Earned: ${final - p}")
