"""
Python OOP: __init__ and Object Initialization
===============================================

Topic: Constructors, initialization, default values

Real-World Applications:
- Object setup
- Required vs optional parameters
- Validation during creation
"""

from typing import Optional
from datetime import datetime


class User:
    """User with proper initialization."""
    
    def __init__(self, username: str, email: str, role: str = "user"):
        """
        Initialize user.
        
        Args:
            username: Username (required)
            email: Email address (required)
            role: User role (optional, defaults to "user")
        """
        self.username = username
        self.email = email
        self.role = role
        self.created_at = datetime.now()
    
    def __repr__(self) -> str:
        return f"User(username='{self.username}', role='{self.role}')"


class DatabaseConnection:
    """Database connection with validation."""
    
    def __init__(self, host: str, port: int = 5432, database: str = "app_db"):
        # Validation
        if port < 1 or port > 65535:
            raise ValueError(f"Invalid port: {port}")
        
        self.host = host
        self.port = port
        self.database = database
        self.connected = False
    
    def connect(self):
        """Simulate connection."""
        self.connected = True
        print(f"Connected to {self.host}:{self.port}/{self.database}")


def main():
    """Demonstrates __init__."""
    print("="*70)
    print("__init__ AND INITIALIZATION".center(70))
    print("="*70)
    
    print("\n[1] REQUIRED PARAMETERS")
    print("-" * 70)
    
    user1 = User("alice", "alice@example.com")
    print(user1)
    
    print("\n[2] OPTIONAL PARAMETERS")
    print("-" * 70)
    
    user2 = User("bob", "bob@example.com", role="admin")
    print(user2)
    
    print("\n[3] INITIALIZATION WITH VALIDATION")
    print("-" * 70)
    
    try:
        db = DatabaseConnection("localhost", port=99999)  # Invalid
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    db = DatabaseConnection("localhost", port=5432)
    db.connect()
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• __init__ initializes new instances")
    print("• Use default parameters for optional values")
    print("• Validate inputs during initialization")
    print("• __init__ doesn't return anything (returns None)")
    print("="*70)


if __name__ == "__main__":
    main()