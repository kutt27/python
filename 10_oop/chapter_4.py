"""
Python OOP: self and Instance Methods
======================================

Topic: The self parameter, instance methods, method calls

Real-World Applications:
- Object behavior
- Encapsulation
- State modification
"""


class Account:
    """Bank account with instance methods."""
    
    def __init__(self, account_id: int, balance: float = 0):
        self.account_id = account_id
        self.balance = balance
    
    def deposit(self, amount: float):
        """Deposit money."""
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money if sufficient balance."""
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_info(self) -> str:
        """Get account information."""
        return f"Account {self.account_id}: ${self.balance:.2f}"


def main():
    """Demonstrates self and instance methods."""
    print("="*70)
    print("SELF & INSTANCE METHODS".center(70))
    print("="*70)
    
    print("\n[1] CREATING INSTANCES")
    print("-" * 70)
    
    account1 = Account(101, 1000.0)
    account2 = Account(102, 500.0)
    
    print(account1.get_info())
    print(account2.get_info())
    
    print("\n[2] CALLING INSTANCE METHODS")
    print("-" * 70)
    
    # Deposit
    new_balance = account1.deposit(500)
    print(f"After deposit: {account1.get_info()}")
    
    # Withdraw
    success = account1.withdraw(300)
    print(f"Withdrawal {'successful' if success else 'failed'}")
    print(f"After withdrawal: {account1.get_info()}")
    
    print("\n[3] SELF IS AUTOMATIC")
    print("-" * 70)
    
    # These are equivalent:
    print("account1.get_info():", account1.get_info())
    print("Account.get_info(account1):", Account.get_info(account1))
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• self is the instance calling the method")
    print("• Python passes self automatically")
    print("• Instance methods can access/modify instance state")
    print("="*70)


if __name__ == "__main__":
    main()