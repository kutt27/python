"""
Topic: Creating BaseModels.

Pydantic models are defined by inheriting from `BaseModel` and using standard Python type hints for fields.
"""

from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True  # Default value

if __name__ == "__main__":
    # Create an instance
    user = User(id=1, username="alice", email="alice@example.com")
    
    # Access attributes like a normal object
    print(f"User ID: {user.id}")
    print(f"Username: {user.username}")
    print(f"Active: {user.is_active}")
