"""
Python OOP: Dataclasses
========================

Topic: @dataclass decorator for simplified classes

Real-World Applications:
- Data transfer objects (DTOs)
- Configuration classes
- API request/response models
- Database models
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import List
from datetime import datetime


@dataclass
class User:
    """User model with dataclass."""
    username: str
    email: str
    role: str = "user"  # Default value
    
    # Automatically generates:
    # __init__, __repr__, __eq__, __hash__ (optional)


@dataclass
class Product:
    """Product with field configuration."""
    name: str
    price: float
    sku: str = field(default_factory=lambda: f"SKU-{datetime.now().timestamp()}")
    tags: List[str] = field(default_factory=list)  # Mutable default
    
    def __post_init__(self):
        """Called after __init__."""
        if self.price < 0:
            raise ValueError("Price cannot be negative")


@dataclass(frozen=True)
class Config:
    """Immutable configuration (frozen)."""
    api_url: str
    timeout: int = 30
    debug: bool = False


@dataclass(order=True)
class Task:
    """Task with automatic ordering."""
    priority: int
    name: str = field(compare=False)  # Exclude from comparison
    completed: bool = field(default=False, compare=False)


def main():
    """Demonstrates dataclasses."""
    print("="*70)
    print("DATACLASSES".center(70))
    print("="*70)
    
    print("\n[1] BASIC DATACLASS")
    print("-" * 70)
    
    user1 = User("alice", "alice@example.com")
    user2 = User("bob", "bob@example.com", role="admin")
    
    print(user1)  # Auto-generated __repr__
    print(user2)
    
    print(f"\nuser1 == user2: {user1 == user2}")  # Auto-generated __eq__
    
    print("\n[2] FIELD CONFIGURATION")
    print("-" * 70)
    
    product = Product("Laptop", 999.99)
    print(product)
    print(f"Auto-generated SKU: {product.sku}")
    
    product.tags.append("electronics")
    product.tags.append("computers")
    print(f"Tags: {product.tags}")
    
    print("\n[3] CONVERSION TO DICT/TUPLE")
    print("-" * 70)
    
    user_dict = asdict(user1)
    print(f"As dict: {user_dict}")
    
    user_tuple = astuple(user1)
    print(f"As tuple: {user_tuple}")
    
    print("\n[4] FROZEN (IMMUTABLE)")
    print("-" * 70)
    
    config = Config("https://api.example.com", timeout=60)
    print(config)
    
    try:
        config.timeout = 120  # Try to modify
    except Exception as e:
        print(f"✗ Cannot modify frozen dataclass: {type(e).__name__}")
    
    print("\n[5] ORDERING")
    print("-" * 70)
    
    tasks = [
        Task(priority=3, name="Low priority task"),
        Task(priority=1, name="Critical task"),
        Task(priority=2, name="Medium task"),
    ]
    
    sorted_tasks = sorted(tasks)
    print("Tasks sorted by priority:")
    for task in sorted_tasks:
        print(f"  {task.priority}: {task.name}")
    
    print("\n" + "="*70)
    print("Dataclass Benefits:")
    print("-" * 70)
    print("✓ Less boilerplate code")
    print("✓ Auto-generates __init__, __repr__, __eq__")
    print("✓ Type hints integrated")
    print("✓ Mutable defaults handled safely")
    print("✓ Optional: frozen, order, slots")
    print("\nCommon Parameters:")
    print("  @dataclass(frozen=True)  # Immutable")
    print("  @dataclass(order=True)   # Enable <, >, etc.")
    print("  @dataclass(slots=True)   # Memory optimization")
    print("="*70)


if __name__ == "__main__":
    main()
