"""
Demonstrates mathematical set operations: Union, Intersection, Difference, and Symmetric Difference.
"""

def demonstrate_set_math() -> None:
    prod = {"auth", "search", "checkout", "analytics"}
    beta = {"checkout", "recommendations", "dark_mode", "ai_chat"}
    
    print(f"Production: {prod}")
    print(f"Beta: {beta}")
    
    print(f"\nUnion (All): {prod | beta}")
    print(f"Intersection (Tested in both): {prod & beta}")
    print(f"Difference (Prod only): {prod - beta}")
    print(f"Symmetric Difference (Unique to one): {prod ^ beta}")

if __name__ == "__main__":
    demonstrate_set_math()
