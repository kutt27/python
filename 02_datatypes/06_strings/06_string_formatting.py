"""
Demonstrates advanced f-string formatting techniques.
"""

def demonstrate_formatting() -> None:
    service = "AuthService"
    uptime = 168.567
    requests = 1_234_567
    error_rate = 0.0023
    
    print(f"Service: {service}")
    print(f"Uptime: {uptime:.1f} hours")
    print(f"Requests: {requests:,}")
    print(f"Error Rate: {error_rate:.2%}")
    print(f"Status: {'HEALTHY' if error_rate < 0.01 else 'DEGRADED'}")
    
    # Padding
    print(f"\nAligned Name: |{service:>20}|")
    print(f"Zero-padded:  {42:05d}")

if __name__ == "__main__":
    demonstrate_formatting()
