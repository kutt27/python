"""
Topic: The `self` Parameter.

`self` refers to the specific instance of the class that the method 
is being called on. It allows methods to access and modify 
the instance's own state.
"""

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount: float):
        """Method using 'self' to update balance."""
        print(f"Depositing {amount} for {self.owner}...")
        self.balance += amount
        
    def check_balance(self):
        print(f"{self.owner}'s Balance: ${self.balance:.2f}")

if __name__ == "__main__":
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 500)
    
    # 'self' is passed automatically by Python
    acc1.deposit(200)
    acc1.check_balance()
    
    # acc2 remains unchanged
    acc2.check_balance()
    
    # Manual call showing what 'self' actually is:
    BankAccount.check_balance(acc1) 
