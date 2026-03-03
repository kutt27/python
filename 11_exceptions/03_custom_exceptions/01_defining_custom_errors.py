"""
Topic: Defining Custom Exceptions.

To create a custom exception, inherit from the built-in `Exception` 
class. This allows your code to signal domain-specific errors 
that are clearer than generic ones.
"""

class InsufficientFundsError(Exception):
    """Raised when an account balance is too low."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw ${amount}. Balance is only ${balance}.")
    return balance - amount

if __name__ == "__main__":
    try:
        new_balance = withdraw(100, 150)
    except InsufficientFundsError as e:
        print(f"Transaction Failed: {e}")
