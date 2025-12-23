"""
Python OOP: Class Methods
==========================

Topic: @classmethod decorator, alternative constructors

Real-World Applications:
- Factory methods
- Alternative constructors
- Class-level operations
"""

from datetime import datetime


class User:
    """User class with factory methods."""
    
    total_users = 0  # Class variable
    
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        User.total_users += 1
    
    @classmethod
    def from_dict(cls, data: dict):
        """Factory: create user from dictionary."""
        return cls(data["username"], data["email"])
    
    @classmethod
    def from_csv_row(cls, csv_row: str):
        """Factory: create user from CSV row."""
        username, email = csv_row.split(",")
        return cls(username.strip(), email.strip())
    
    @classmethod
    def get_total_users(cls) -> int:
        """Get total user count."""
        return cls.total_users
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Config:
    """Configuration with class methods."""
    
    _instance = None
    
    def __init__(self):
        self.settings = {}
    
    @classmethod
    def get_instance(cls):
        """Singleton pattern."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


def main():
    """Demonstrates class methods."""
    print("="*70)
    print("CLASS METHODS".center(70))
    print("="*70)
    
    print("\n[1] ALTERNATIVE CONSTRUCTORS")
    print("-" * 70)
    
    # Regular constructor
    user1 = User("alice", "alice@example.com")
    print(f"Regular: {user1}")
    
    # From dictionary
    user_data = {"username": "bob", "email": "bob@example.com"}
    user2 = User.from_dict(user_data)
    print(f"From dict: {user2}")
    
    # From CSV
    csv_row = "charlie, charlie@example.com"
    user3 = User.from_csv_row(csv_row)
    print(f"From CSV: {user3}")
    
    print("\n[2] CLASS-LEVEL OPERATIONS")
    print("-" * 70)
    
    print(f"Total users created: {User.get_total_users()}")
    
    print("\n[3] SINGLETON PATTERN")
    print("-" * 70)
    
    config1 = Config.get_instance()
    config2 = Config.get_instance()
    
    print(f"Same instance? {config1 is config2}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Class methods receive 'cls' as first parameter")
    print("• Called via ClassName.method()")
    print("• Use for alternative constructors (factory methods)")
    print("• Access/modify class-level state")
    print("="*70)


if __name__ == "__main__":
    main()