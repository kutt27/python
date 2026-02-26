"""
Topic: Input Data Validation.

Decorators can perform "pre-flight" checks on arguments to 
ensure they meet specific criteria (like being positive numbers) 
before the main logic proceeds.
"""

from functools import wraps

def ensure_positive(func):
    """Enforces that all numeric arguments must be > 0."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Invalid input: {arg}. Values must be positive.")
        return func(*args, **kwargs)
    return wrapper

@ensure_positive
def calculate_discount(price, pct):
    return price * (pct / 100)

if __name__ == "__main__":
    print(f"Discount: ${calculate_discount(100, 10)}")
    
    try:
        calculate_discount(100, -5) # This will fail
    except ValueError as e:
        print(f"Caught expected error: {e}")
