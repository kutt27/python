"""
Topic: Exception Payloads.

Custom exceptions can store additional data in their `__init__` 
method, which can be extracted by the code catching the exception.
"""

class ValidationError(Exception):
    def __init__(self, message, field_name, invalid_value):
        super().__init__(message)
        self.field_name = field_name
        self.invalid_value = invalid_value

def validate_user(username):
    if len(username) < 3:
        raise ValidationError("Username too short", "username", username)

if __name__ == "__main__":
    try:
        validate_user("ab")
    except ValidationError as e:
        print(f"Error: {e}")
        print(f"Field: {e.field_name}")
        print(f"Value: {e.invalid_value}")
