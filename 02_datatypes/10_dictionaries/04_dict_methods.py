"""
Demonstrates iterating over dictionary keys, values, and items.
"""

def demonstrate_methods() -> None:
    status = {"api": "up", "db": "up", "cache": "down"}
    
    print(f"Keys:   {list(status.keys())}")
    print(f"Values: {list(status.values())}")
    
    print("\nItems:")
    for key, val in status.items():
        print(f"  {key}: {val}")

if __name__ == "__main__":
    demonstrate_methods()
