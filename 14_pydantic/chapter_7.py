"""
Pydantic: Model Configuration
==============================

Topic: ConfigDict and strict mode

Real-World Applications:
- Forbidding extra fields (strict API validation)
- Immutability (frozen models)
- Stripping whitespace
"""

from pydantic import BaseModel, ConfigDict, ValidationError

class StrictUser(BaseModel):
    """
    User model with strict configuration.
    """
    model_config = ConfigDict(
        frozen=True,        # Immutable (like dataclass frozen)
        extra='forbid',     # Error on unknown fields
        str_strip_whitespace=True # Auto-trim strings
    )
    
    username: str
    age: int


def main():
    """Demonstrates model config."""
    print("="*70)
    print("MODEL CONFIGURATION".center(70))
    print("="*70)
    
    print("\n[1] Whitespace Stripping")
    user = StrictUser(username="  alice  ", age=30)
    print(f"Username: '{user.username}' (Stripped)")
    
    print("\n[2] Extra Fields (Forbid)")
    try:
        StrictUser(username="bob", age=25, is_admin=True)
    except ValidationError as e:
        print(f"✗ Error: {e.errors()[0]['type']} - {e.errors()[0]['msg']}")
    
    print("\n[3] Immutability (Frozen)")
    try:
        user.age = 31
    except ValidationError as e:
        print("✗ Error: Cannot assign to field 'age' (frozen instance)")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Use `model_config = ConfigDict(...)` inside model")
    print("• `extra='ignore'|'allow'|'forbid'` controls unknown keys")
    print("• `frozen=True` makes instances immutable (hashable)")
    print("• `str_strip_whitespace=True` cleans input data")
    print("="*70)


if __name__ == "__main__":
    main()
