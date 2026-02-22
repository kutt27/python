"""
Topic: Pure Functions.

Characteristics:
1. Deterministic: Same input always results in the same output.
2. No Side Effects: Does not modify external state or perform I/O.
"""

def add(a: int, b: int) -> int:
    """Pure: output depends only on inputs."""
    return a + b

def calculate_discount(price: float, pct: float) -> float:
    """Pure: no external variables used."""
    return price * (1 - pct / 100)

if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"100 - 10% = {calculate_discount(100, 10)}")
    
    # Pure functions are easy to test because they are predictable.
