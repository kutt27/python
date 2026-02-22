"""
Topic: Stateful Closures with `nonlocal`.

The `nonlocal` keyword allows a nested function to modify 
a variable in its enclosing scope, enabling stateful functions 
without using classes.
"""

def create_counter():
    """Initializes a counter with an enclosing variable."""
    count = 0
    
    def increment():
        nonlocal count # Allows modifying 'count' from outer scope
        count += 1
        return count
    
    return increment

if __name__ == "__main__":
    counterA = create_counter()
    counterB = create_counter()
    
    print(f"A: {counterA()}")
    print(f"A: {counterA()}")
    print(f"B: {counterB()}") # Independent state
    print(f"A: {counterA()}")
