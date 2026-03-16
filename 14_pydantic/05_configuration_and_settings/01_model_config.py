"""
Topic: Model Configuration (ConfigDict).

Use `model_config = ConfigDict(...)` to change how Pydantic behaves.
You can forbid extra fields, make the model immutable (frozen), or 
automatically strip the whitespace from strings.
"""

from pydantic import BaseModel, ConfigDict, ValidationError

class StrictUser(BaseModel):
    model_config = ConfigDict(
        frozen=True,              # Immutable objects
        extra='forbid',           # Throw error on extra fields
        str_strip_whitespace=True # Trim strings automatically
    )
    
    username: str

if __name__ == "__main__":
    # Test whitespace stripping
    u = StrictUser(username="   alice   ")
    print(f"Stripped Username: '{u.username}'")

    print("-" * 30)

    # Test extra field
    try:
        StrictUser(username="bob", is_admin=True)
    except ValidationError as e:
        print("Extra Error:")
        print(f"  {e.errors()[0]['msg']}")

    print("-" * 30)

    # Test mutability
    try:
        u.username = "charlie"
    except ValidationError as e:
        print("Mutation Error:")
        print(f"  Cannot modify a frozen model")
