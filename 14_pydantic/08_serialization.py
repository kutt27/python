"""
Pydantic: Serialization
========================

Topic: model_dump, model_dump_json, include/exclude

Real-World Applications:
- Hiding sensitive fields (passwords)
- Exporting for database vs API
- Alias handling
"""

from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    username: str
    password: str = Field(exclude=True) # Always exclude from dump
    bio: str = "No bio"

def main():
    """Demonstrates serialization options."""
    print("="*70)
    print("SERIALIZATION TECHNIQUES".center(70))
    print("="*70)
    
    user = User(id=1, username="admin", password="secret_password")
    
    print("\n[1] Default Dump (Password excluded via Field)")
    print(user.model_dump())
    
    print("\n[2] Include/Exclude at runtime")
    # Only sending minimal info
    print(user.model_dump(include={'username', 'id'}))
    
    print("\n[3] JSON Export")
    print(user.model_dump_json())
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• `model_dump()` returns a python dict")
    print("• `model_dump_json()` returns a JSON string")
    print("• `exclude=True` in Field hides it by default")
    print("• `include={...}` / `exclude={...}` allows dynamic filtering")
    print("="*70)


if __name__ == "__main__":
    main()
