"""
Pydantic: Nested Models
========================

Topic: Building complex hierarchies with schemas

Real-World Applications:
- JSON API Responses
- Complex Configuration
- Document Databases (MongoDB)
"""

from pydantic import BaseModel, Field
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class OrderItem(BaseModel):
    product_name: str
    quantity: int = Field(gt=0)
    price_per_unit: float

class Order(BaseModel):
    order_id: str
    shipping_address: Address  # Nested Model
    items: List[OrderItem]     # List of Nested Models
    
    @property
    def total_price(self) -> float:
        return sum(item.quantity * item.price_per_unit for item in self.items)


def main():
    """Demonstrates nested models."""
    print("="*70)
    print("NESTED MODELS".center(70))
    print("="*70)
    
    # 1. Define Data (simulating JSON payload)
    payload = {
        "order_id": "ORD-999",
        "shipping_address": {
            "street": "123 Python Lane",
            "city": "Coding City",
            "zip_code": "10101"
        },
        "items": [
            {"product_name": "Keyboard", "quantity": 1, "price_per_unit": 50.0},
            {"product_name": "Mouse", "quantity": 2, "price_per_unit": 25.0}
        ]
    }
    
    print("\n[1] Parsing Complex Data")
    order = Order(**payload)
    
    print(f"Order ID: {order.order_id}")
    print(f"City: {order.shipping_address.city}")
    print(f"Item 2: {order.items[1].product_name}")
    
    print("\n[2] Computed Total (Property)")
    print(f"Total: ${order.total_price:.2f}")
    
    print("\n[3] Exporting back to JSON")
    # model_dump handles recursion automatically
    print(order.model_dump_json(indent=2))
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Models can be used as types for fields")
    print("• `List[Model]` creates a list of validated objects")
    print("• Pydantic parses nested dictionaries automatically")
    print("="*70)


if __name__ == "__main__":
    main()
