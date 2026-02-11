"""
Demonstrates basic floating-point operations.
"""

def demonstrate_float_basics() -> None:
    # Example: Server temperature monitoring
    target_temp = 65.5
    current_temp = 65.49
    
    diff = target_temp - current_temp
    print(f"Target: {target_temp}°C, Current: {current_temp}°C")
    print(f"Difference: {diff}°C")
    
    # Check with tolerance
    tolerance = 0.5
    print(f"Within tolerance (±0.5)? {abs(diff) <= tolerance}")

if __name__ == "__main__":
    demonstrate_float_basics()
