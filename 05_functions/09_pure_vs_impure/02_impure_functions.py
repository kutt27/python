"""
Topic: Impure Functions and Side Effects.

Impure functions have side effects like:
- Modifying a global variable
- Writing to a file or database
- Printing to the console
- Changing a mutable input (like a list)
"""

LOGS = []

def log_impure(message: str):
    """Side effect: Modifies global LOGS and performs I/O."""
    LOGS.append(message)
    print(f"Log: {message}")

def update_cart_impure(cart: list, item: str):
    """Side effect: Modifies the input list in-place."""
    cart.append(item)

if __name__ == "__main__":
    my_cart = ["apple"]
    update_cart_impure(my_cart, "banana")
    print(f"Cart after side effect: {my_cart}")
    
    log_impure("User added banana to cart")
    print(f"Global logs: {LOGS}")
