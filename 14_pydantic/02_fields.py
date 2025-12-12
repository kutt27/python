"""
Pydantic: Fields & Types
=========================

Topic: Field configuration, constraints, and specialized types

Real-World Applications:
- Constraining numeric ranges (age, price)
- String constraints (regex, length)
- Specialized types (Email, URL, UUID)
"""

from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional
from uuid import UUID, uuid4

class Product(BaseModel):
    """
    Product model with extensive constraints.
    """
    id: UUID = Field(default_factory=uuid4)
    
    name: str = Field(
        ..., 
        min_length=3, 
        max_length=50, 
        description="Product name (3-50 chars)"
    )
    
    sku: str = Field(..., pattern=r"^[A-Z]{3}-\d{4}$") # Regex: ABC-1234
    
    price: float = Field(..., gt=0, decimal_places=2) # Greater than 0
    
    stock: int = Field(default=0, ge=0) # Greater or equal to 0
    
    tags: list[str] = Field(default_factory=list, max_length=5)
    

class Vendor(BaseModel):
    """Vendor using Pydantic Types."""
    name: str
    email: EmailStr # Requires 'pip install pydantic[email]'
    website: HttpUrl


def main():
    """Demonstrates Field constraints."""
    print("="*70)
    print("PYDANTIC FIELDS & CONSTRAINTS".center(70))
    print("="*70)
    
    print("\n[1] Field Constraints")
    try:
        p = Product(
            name="A", # Too short
            sku="INVALID", # Wrong regex
            price=-10.0 # Negative
        )
    except Exception as e:
        # Just showing the wrapper, catching ValidationError typically
        print(f"Validation Error: {e}")
        
    # Valid Product
    p_valid = Product(
        name="Gaming Laptop",
        sku="GAM-2024",
        price=1299.99,
        stock=5
    )
    print(f"Valid Product: {p_valid.name} (${p_valid.price})")
    
    print("\n[2] Specialized Types (Email/URL)")
    try:
        v = Vendor(
            name="Acme Corp",
            email="not-an-email", 
            website="ht tp://bad-url"
        )
    except Exception as e:
        print("✗ Invalid Types caught!")
        
    v_valid = Vendor(
        name="Tech Corp",
        email="contact@tech.com",
        website="https://tech.com"
    )
    print(f"Valid Vendor: {v_valid.email} | {v_valid.website}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Use `Field(...)` for metadata and constraints")
    print("• Numeric: gt ( > ), ge ( >= ), lt ( < ), le ( <= )")
    print("• String: min_length, max_length, pattern (regex)")
    print("• Pydantic provides EmailStr, HttpUrl, IPvAnyAddress, etc.")
    print("="*70)


if __name__ == "__main__":
    main()
