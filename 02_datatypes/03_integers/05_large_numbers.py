"""
Demonstrates Python's arbitrary precision integers and readability features.
"""

def demonstrate_large_numbers() -> None:
    # Underscores for readability (Python 3.6+)
    daily_requests = 1_000_000_000  # 1 billion
    days_in_year = 365
    
    annual_requests = daily_requests * days_in_year
    print(f"Annual API requests: {annual_requests:,}")
    print(f"Formatted with underscores: {annual_requests:_}")
    
    # Large calculation (Python handles this automatically)
    power_of_two = 2 ** 1000
    print(f"\n2^1000 has {len(str(power_of_two))} digits")

if __name__ == "__main__":
    demonstrate_large_numbers()
