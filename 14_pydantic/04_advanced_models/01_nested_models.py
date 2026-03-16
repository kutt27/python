"""
Topic: Nested Models.

Use other Pydantic models as types to create deep, nested structures.
Pydantic easily parses JSON into nested object hierarchies.
"""

from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class OrderItem(BaseModel):
    product: str
    quantity: int

class Order(BaseModel):
    order_id: str
    shipping_address: Address # Nested directly
    items: List[OrderItem]    # List of nested

if __name__ == "__main__":
    payload = {
        "order_id": "ORD-123",
        "shipping_address": {
            "street": "123 Main St",
            "city": "Anytown",
            "zip_code": "12345"
        },
        "items": [
            {"product": "Book", "quantity": 1},
            {"product": "Pen", "quantity": 5}
        ]
    }
    
    # Automatically parses nested dicts into models
    order = Order(**payload)
    print(f"Order ID: {order.order_id}")
    print(f"City: {order.shipping_address.city}")
    print(f"Product 2: {order.items[1].product}")
