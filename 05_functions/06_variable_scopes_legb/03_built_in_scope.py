"""
Topic: Built-in Scope.

Python's built-in functions (like len, max, min, print) 
reside in a special scope that is always available.
"""

def check_builtins():
    data = [1, 5, 2]
    
    # len and max are built-in functions
    print(f"Length: {len(data)}")
    print(f"Max: {max(data)}")

if __name__ == "__main__":
    check_builtins()
    
    # Note: avoid naming variables after built-ins!
    # list = [1, 2] # This "shadows" the built-in 'list' type
