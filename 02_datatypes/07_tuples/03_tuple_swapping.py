"""
Demonstrates the idiomatic way to swap variable values using tuples.
"""

def demonstrate_swapping() -> None:
    primary = "server-a"
    secondary = "server-b"
    
    print(f"Before: Primary={primary}, Secondary={secondary}")
    
    # Pythonic swap
    primary, secondary = secondary, primary
    
    print(f"After:  Primary={primary}, Secondary={secondary}")

if __name__ == "__main__":
    demonstrate_swapping()
