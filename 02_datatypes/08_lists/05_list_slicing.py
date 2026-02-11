"""
Demonstrates list slicing for pagination and sub-sampling.
"""

def demonstrate_slicing() -> None:
    records = list(range(1, 11))
    print(f"Records: {records}")
    
    # First 3
    print(f"First 3: {records[:3]}")
    
    # Page 2 (items 4-6)
    print(f"Items 4-6: {records[3:6]}")
    
    # Last 2
    print(f"Last 2: {records[-2:]}")
    
    # Every 2nd item
    print(f"Step 2: {records[::2]}")

if __name__ == "__main__":
    demonstrate_slicing()
