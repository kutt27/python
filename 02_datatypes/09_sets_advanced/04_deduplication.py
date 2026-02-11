"""
Demonstrates using sets to remove duplicates from lists.
"""

def demonstrate_deduplication() -> None:
    source_a = [101, 102, 103, 101, 102]
    source_b = [103, 104, 105, 104]
    
    unique_a = set(source_a)
    print(f"Unique A: {unique_a}")
    
    all_unique = set(source_a) | set(source_b)
    print(f"All Unique from A & B: {sorted(all_unique)}")

if __name__ == "__main__":
    demonstrate_deduplication()
