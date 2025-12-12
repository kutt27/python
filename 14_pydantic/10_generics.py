"""
Pydantic: Generic Models
=========================

Topic: Generic[T] with Pydantic

Real-World Applications:
- Standard API Response Envelopes
- Paginated Results
"""

from pydantic import BaseModel
from typing import Generic, TypeVar, List

T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
    """
    Generic Response Wrapper.
    """
    status: str
    data: T
    meta: dict = {}

class User(BaseModel):
    name: str

class Product(BaseModel):
    sku: str
    price: float

def main():
    """Demonstrates generics."""
    print("="*70)
    print("GENERIC MODELS".center(70))
    print("="*70)
    
    # 1. Response with User data
    user = User(name="Alice")
    response_user = APIResponse[User](
        status="success", 
        data=user
    )
    print(f"User Response: {response_user.data.name}")
    
    # 2. Response with Product list
    products = [Product(sku="A", price=10), Product(sku="B", price=20)]
    response_products = APIResponse[List[Product]](
        status="success",
        data=products
    )
    print(f"Product Response: {len(response_products.data)} items")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Inherit from `BaseModel, Generic[T]`")
    print("• Allows reusable envelopes (standard JSON formats)")
    print("• Static type checkers (mypy) understand this perfectly")
    print("="*70)


if __name__ == "__main__":
    main()
