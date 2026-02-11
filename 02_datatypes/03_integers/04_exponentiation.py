"""
Demonstrates exponentiation (**) for scaling and exponential growth.
"""

def demonstrate_exponentiation() -> None:
    # Example: Exponential backoff for API retry logic
    base_delay_seconds = 2
    retry_attempt = 3
    
    # Calculate delay: 2^3 = 8 seconds
    retry_delay = base_delay_seconds ** retry_attempt
    print(f"Retry delay for attempt {retry_attempt}: {retry_delay} seconds")
    
    # Growth projection
    initial_records = 1000
    growth_rate = 2
    print("\nData growth projection:")
    for period in range(1, 4):
        projected = initial_records * (growth_rate ** period)
        print(f"Period {period}: {projected:,} records")

if __name__ == "__main__":
    demonstrate_exponentiation()
