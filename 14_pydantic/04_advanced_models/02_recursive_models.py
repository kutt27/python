"""
Topic: Recursive Models.

Models can reference themselves using a string forward-reference. 
This is useful for hierarchical data like trees or comments.
"""

from pydantic import BaseModel
from typing import List

class Category(BaseModel):
    name: str
    # Forward refer to the same class name as string Let's use string
    sub_categories: List['Category'] = []

if __name__ == "__main__":
    root = Category(
        name="Electronics",
        sub_categories=[
            Category(
                name="Computers",
                sub_categories=[
                    Category(name="Laptops"),
                    Category(name="Desktops")
                ]
            ),
            Category(name="Cameras")
        ]
    )
    
    print(f"Root: {root.name}")
    print(f"First Child: {root.sub_categories[0].name}")
    print(f"First Grandchild: {root.sub_categories[0].sub_categories[0].name}")
