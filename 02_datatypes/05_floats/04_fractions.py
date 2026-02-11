"""
Demonstrates the Fraction type for exact rational number calculations.
"""

from fractions import Fraction

def demonstrate_fractions() -> None:
    # Example: Rate limiting
    reqs = 100
    secs = 60
    rate = Fraction(reqs, secs)
    
    print(f"Rate: {reqs} reqs / {secs} secs = {rate} reqs/sec")
    print(f"As float: {float(rate):.4f}")
    
    # Load distribution among 3 services
    load = 1000
    per_service = Fraction(load, 3)
    print(f"\nLoad per service (1000 / 3): {per_service}")
    print(f"As float: {float(per_service):.2f}")

if __name__ == "__main__":
    demonstrate_fractions()
