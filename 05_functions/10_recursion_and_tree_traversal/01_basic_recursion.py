"""
Topic: Basic Recursion.

A function that calls itself to solve a smaller version of 
the problem. Must have a base case to stop the recursion.
"""

def factorial(n: int) -> int:
    """Calculates n! using recursion."""
    # Base case
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial(n - 1)

if __name__ == "__main__":
    for i in range(1, 6):
        print(f"{i}! = {factorial(i)}")
