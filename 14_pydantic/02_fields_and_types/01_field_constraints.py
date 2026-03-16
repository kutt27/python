"""
Topic: Field Constraints.

Use Pydantic's `Field` to define constraints, defaults, and 
metadata for individual fields. Use constraints like `gt`, `ge`, 
`lt`, `le` for numbers, and `min_length`, `max_length`, `pattern` 
for strings.
"""

from pydantic import BaseModel, Field

class Product(BaseModel):
    # Required string with length constraints
    name: str = Field(..., min_length=3, max_length=50)
    
    # Required string matching a regex pattern
    sku: str = Field(..., pattern=r"^[A-Z]{3}-\d{4}$")
    
    # Required float greater than 0
    price: float = Field(..., gt=0)
    
    # Optional int with a default, must be non-negative
    stock: int = Field(default=0, ge=0)

if __name__ == "__main__":
    p_valid = Product(name="Gaming Laptop", sku="GAM-2024", price=1299.99, stock=5)
    print(f"Valid Product: {p_valid.name} (${p_valid.price})")
