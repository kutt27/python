"""
Topic: Visualizing Recursion Depth.

Using indentation to show the call stack depth during recursion.
"""

def fib(n: int, depth: int = 0) -> int:
    """Calculates nth Fibonacci number with a visual trace."""
    indent = "  " * depth
    print(f"{indent}→ fib({n})")
    
    if n <= 1:
        print(f"{indent}← {n}")
        return n
    
    result = fib(n - 1, depth + 1) + fib(n - 2, depth + 1)
    print(f"{indent}← {result}")
    return result

if __name__ == "__main__":
    print("\nTracing Fibonacci(4):")
    fib(4)
