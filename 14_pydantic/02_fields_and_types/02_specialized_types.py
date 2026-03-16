"""
Topic: Specialized Types.

Pydantic provides specialized types out of the box that provide 
automatic validation for common patterns like emails, URLs, and UUIDs.
Note: Email validation requires installing 'pydantic[email]'.
"""

from pydantic import BaseModel, EmailStr, HttpUrl
from uuid import UUID, uuid4

class Vendor(BaseModel):
    # This automatically requires a valid UUID
    id: UUID
    
    # This requires 'pip install pydantic[email]' to work properly
    email: EmailStr
    
    # Parses strings and validates that it's a well-formed http/https URL
    website: HttpUrl

if __name__ == "__main__":
    v_valid = Vendor(
        id=uuid4(),
        email="contact@tech.com",
        website="https://tech.com"
    )
    
    print(f"Valid Vendor ID: {v_valid.id}")
    print(f"Email: {v_valid.email}")
    print(f"Website Scheme: {v_valid.website.scheme}")
    print(f"Website Host: {v_valid.website.host}")
