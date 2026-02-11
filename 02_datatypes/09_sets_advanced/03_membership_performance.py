"""
Demonstrates that set membership testing is O(1) and very efficient.
"""

def demonstrate_performance() -> None:
    allowed_ips = {"192.168.1.10", "192.168.1.20", "10.0.0.5"}
    
    incoming = "192.168.1.10"
    print(f"IP {incoming} allowed? {incoming in allowed_ips}")
    
    # Context
    print("\nNote: Set membership is O(1), while Lists are O(n).")

if __name__ == "__main__":
    demonstrate_performance()
