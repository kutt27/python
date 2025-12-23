"""
Python OOP: Property Decorators
================================

Topic: @property, getters/setters, computed attributes

Real-World Applications:
- Controlled attribute access
- Validation
- Computed properties
- Encapsulation
"""


class Temperature:
    """Temperature with Celsius/Fahrenheit conversion."""
    
    def __init__(self, celsius: float = 0):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float):
        """Set temperature in Celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        """Get temperature in Fahrenheit (computed)."""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float):
        """Set temperature via Fahrenheit."""
        self.celsius = (value - 32) * 5/9


class BankAccount:
    """Bank account with validation."""
    
    def __init__(self, account_number: str, initial_balance: float = 0):
        self._account_number = account_number
        self._balance = initial_balance
    
    @property
    def balance(self) -> float:
        """Get account balance (read-only)."""
        return self._balance
    
    @property
    def account_number(self) -> str:
        """Get masked account number."""
        return f"****{self._account_number[-4:]}"
    
    def deposit(self, amount: float):
        """Deposit money."""
        if amount > 0:
            self._balance += amount


def main():
    """Demonstrates properties."""
    print("="*70)
    print("PROPERTY DECORATORS".center(70))
    print("="*70)
    
    print("\n[1] BASIC PROPERTIES")
    print("-" * 70)
    
    temp = Temperature(25)
    print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")
    
    # Set via Fahrenheit
    temp.fahrenheit = 68
    print(f"After setting to 68°F: {temp.celsius}°C")
    
    print("\n[2] VALIDATION")
    print("-" * 70)
    
    try:
        temp.celsius = -300  # Below absolute zero
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    print("\n[3] READ-ONLY PROPERTIES")
    print("-" * 70)
    
    account = BankAccount("1234567890", 1000)
    print(f"Account: {account.account_number}")
    print(f"Balance: ${account.balance:.2f}")
    
    account.deposit(500)
    print(f"After deposit: ${account.balance:.2f}")
    
    # Can't directly set balance
    # account.balance = 9999  # Would raise AttributeError
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• @property makes method accessible like attribute")
    print("• @prop.setter adds validation/logic")
    print("• Computed properties: calculated on access")
    print("• Read-only: property without setter")
    print("• Encapsulation: hide implementation details")
    print("="*70)


if __name__ == "__main__":
    main()
