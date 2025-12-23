"""
Pydantic: Recursive Models
===========================

Topic: Self-referencing models

Real-World Applications:
- Comment threads (Reddit style)
- Organization charts
- Category trees
- File systems
"""

from pydantic import BaseModel
from typing import List, Optional

class Category(BaseModel):
    """Recursive Category Tree."""
    id: int
    name: str
    sub_categories: List['Category'] = [] # Forward reference
    
    # Note: In methods, 'Category' is available
    def list_all_names(self) -> List[str]:
        names = [self.name]
        for sub in self.sub_categories:
            names.extend(sub.list_all_names())
        return names


def main():
    """Demonstrates recursion."""
    print("="*70)
    print("RECURSIVE MODELS".center(70))
    print("="*70)
    
    # Creating a tree structure
    electronics = Category(
        id=1, 
        name="Electronics",
        sub_categories=[
            Category(
                id=2, 
                name="Computers",
                sub_categories=[
                    Category(id=3, name="Laptops"),
                    Category(id=4, name="Desktops")
                ]
            ),
            Category(id=5, name="Cameras")
        ]
    )
    
    print("\n[1] Tree Structure")
    print(electronics.model_dump_json(indent=2))
    
    print("\n[2] Traversing Tree")
    all_names = electronics.list_all_names()
    print(f"Flattened: {all_names}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Use `List['ClassName']` string forward reference for recursion")
    print("• Pydantic handles infinite depth validation (until stack overflow)")
    print("• Useful for tree-like structures")
    print("="*70)


if __name__ == "__main__":
    main()
