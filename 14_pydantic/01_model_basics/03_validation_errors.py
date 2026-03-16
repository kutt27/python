"""
Topic: Validation Errors.

If Pydantic cannot convert the data or a required field is missing, it raises a `ValidationError`.
"""

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    username: str

if __name__ == "__main__":
    try:
        # Fails because "abc" cannot be converted to int
        User(id="abc", username="charlie")
    except ValidationError as e:
        print("Validation Failed:")
        for error in e.errors():
            print(f"  Field: {error['loc'][0]} -> {error['msg']}")
            
    print("-" * 30)
    
    try:
        # Fails because 'username' is missing
        User(id=2)
    except ValidationError as e:
        print("Missing Field Error:")
        print(f"  {e.errors()[0]['msg']}")
