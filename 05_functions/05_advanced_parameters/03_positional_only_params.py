"""
Topic: Positional-Only Parameters (/).

Parameters before the `/` cannot be passed as keyword 
arguments. This is useful when parameter names don't matter 
or might change.
"""

def power(base, exponent, /):
    """Caller cannot use keywords like power(base=2, exponent=3)."""
    return base ** exponent

if __name__ == "__main__":
    print(f"Result: {power(2, 3)}") # OK
    
    # This would raise a TypeError:
    # power(base=2, exponent=3)
