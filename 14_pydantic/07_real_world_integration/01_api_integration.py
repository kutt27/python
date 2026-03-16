"""
Topic: Complete Data Pipeline Example.

This script simulates a standard backend API flow using Pydantic:
1. Receive raw untyped payload (JSON/Dict)
2. Parse & Validate input (Pydantic Model)
3. Persist to DB or handle logic (Mock DB)
4. Transform DB model to output JSON.
"""

from pydantic import BaseModel, Field, EmailStr

# Input Schema
class CreateUserRequest(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=8)

# Domain Schema
class UserDB(BaseModel):
    id: int
    username: str
    email: str

def api_endpoint(payload: dict):
    """Simulated API Endpoint."""
    print(f"\n[POST /users] Request Payload: {payload}")
    
    try:
        # STEP 1 & 2: Parse and Validate Request
        req = CreateUserRequest(**payload)
        print("  ✓ Request Validation Passed.")
        
        # STEP 3: Business Logic (Simulated DB Insertion)
        db_user = UserDB(
            id=101,
            username=req.username,
            email=req.email
        )
        print("  ✓ User created in DB.")
        
        # STEP 4: Serialization for Response
        # We don't send the password back!
        return {
            "status": "success",
            "data": db_user.model_dump()
        }
        
    except Exception as e:
        print("  ✗ Request Failed.")
        return {"status": "error", "reason": str(e)}

if __name__ == "__main__":
    # Scenario A: Valid request
    res1 = api_endpoint({
        "username": "johndoe",
        "email": "john@example.com",
        "password": "supersecretpassword123"
    })
    print(res1)
    
    print("-" * 50)
    
    # Scenario B: Invalid request (password too short, bad email)
    res2 = api_endpoint({
        "username": "jo",
        "email": "not_an_email",
        "password": "123"
    })
    print(res2)
