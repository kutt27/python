"""
Pydantic: Model Basics (V2 or Higher)
=====================================

Topic: Defining models, basic validation, and type coercion

Real-World Applications:
- API Request Bodies
- Database Schemas
- Configuration Files
"""

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    """
    Basic User Model.
    Pydantic allows standard Python type hints.
    """
    id: int
    username: str
    email: str
    is_active: bool = True  # Default value


def main():
    """Demonstrates basic Pydantic usage."""
    print("="*70)
    print("PYDANTIC BASICS".center(70))
    print("="*70)
    
    # 1. Valid Creation
    print("\n[1] Creating Valid Objects")
    user1 = User(id=1, username="alice", email="alice@example.com")
    print(f"User 1: {user1}")
    print(f"JSON: {user1.model_dump_json()}")
    
    # 2. Type Coercion
    # Pydantic attempts to convert types (e.g., str "2" -> int 2)
    print("\n[2] Type Coercion")
    user2 = User(id="2", username="bob", email="bob@example.com")
    print(f"User 2 ID type: {type(user2.id)} (Value: {user2.id})")
    
    # 3. Validation Errors
    print("\n[3] Validation Errors")
    try:
        User(id="invalid_int", username="charlie", email="charlie@example.com")
    except ValidationError as e:
        print("✗ Validation Failed:")
        # Pretty print errors
        for error in e.errors():
            print(f"  Field: {error['loc'][0]} -> {error['msg']}")
            
    # 4. Missing Fields
    print("\n[4] Missing Fields")
    try:
        User(id=3, username="dave") # Missing email
    except ValidationError as e:
        print("✗ Missing Email Error:")
        print(f"  {e.errors()[0]['msg']}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Inherit from `BaseModel`")
    print("• Define fields with type hints")
    print("• Types are enforced (validated) and coerced (converted)")
    print("• `model_dump()` -> dict, `model_dump_json()` -> json string")
    print("="*70)


if __name__ == "__main__":
    main()
