"""
Topic: Type Coercion.

Pydantic attempts to coerce data into the correct type when possible (e.g., converting a string "123" to an integer 123).
"""

from pydantic import BaseModel

class DataPoint(BaseModel):
    value: int
    status: bool

if __name__ == "__main__":
    # Coercing string to int, and string to bool
    # Pydantic understands common boolean strings like 'yes', 'true', '1'
    data = DataPoint(value="42", status="yes")
    
    print(f"Value type: {type(data.value)} - Value: {data.value}")
    print(f"Status type: {type(data.status)} - Status: {data.status}")
