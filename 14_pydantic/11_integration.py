"""
Pydantic: Integration Example (FastAPI Style)
==============================================

Topic: Putting it all together

Real-World Applications:
- Typical API Endpoint workflow
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# --- Data Models ---
class UserCreate(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=8)

class UserDB(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    
    # Config to allow creating from ORM objects (attributes)
    model_config = {"from_attributes": True}

# --- Simulated Service ---

class MockDB:
    def __init__(self):
        self.users = {}
        self.counter = 1
        
    def create_user(self, user_in: UserCreate) -> UserDB:
        new_id = self.counter
        self.counter += 1
        
        # Simulating DB record creation
        # Note: In real app, hash password here!
        db_user = UserDB(
            id=new_id,
            username=user_in.username,
            email=user_in.email
        )
        self.users[new_id] = db_user
        return db_user

def api_create_user(payload: dict):
    """Simulates an API endpoint."""
    print(f"\n[API] POST /users with {payload}")
    
    try:
        # 1. Parse & Validate
        user_in = UserCreate(**payload)
        print("  ✓ Validation passed")
        
        # 2. Logic
        db = MockDB()
        user_out = db.create_user(user_in)
        
        # 3. Serialize Response
        return user_out.model_dump()
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return {"error": str(e)}

def main():
    """Demonstrates API integration flow."""
    print("="*70)
    print("INTEGRATION EXAMPLE".center(70))
    print("="*70)
    
    # Valid Request
    response = api_create_user({
        "username": "johndoe",
        "email": "john@example.com",
        "password": "supersecretpassword"
    })
    print(f"Response: {response}")
    
    # Invalid Request
    api_create_user({
        "username": "jo", # too short
        "email": "bad-email",
        "password": "123"
    })
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• In FastAPI, this validation happens automatically")
    print("• You define `InputModel` and `OutputModel`")
    print("• Pydantic handles the IO boundaries safely")
    print("="*70)


if __name__ == "__main__":
    main()
