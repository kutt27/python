"""
Demonstrates Counter for efficient frequency counting of hashable objects.
"""

from collections import Counter

def demonstrate_counter() -> None:
    stats = [200, 200, 404, 200, 500, 200, 404]
    counts = Counter(stats)
    
    print(f"Counts: {counts}")
    print(f"Top 2: {counts.most_common(2)}")
    
    # Arithmetic with Counters
    c1 = Counter(["a", "b"])
    c2 = Counter(["a", "c"])
    print(f"Combined: {c1 + c2}")

if __name__ == "__main__":
    demonstrate_counter()
