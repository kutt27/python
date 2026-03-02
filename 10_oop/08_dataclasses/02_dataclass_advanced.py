"""
Topic: Advanced Dataclasses.

Using `field` for mutable defaults, `frozen=True` for immutability, 
and `__post_init__` for validation.
"""

from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Config:
    """Immutable configuration object."""
    port: int
    host: str = "localhost"

@dataclass
class Member:
    name: str
    # 'field(default_factory=list)' is used for mutable defaults like lists
    roles: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Run automatically after __init__."""
        if not self.name:
            raise ValueError("Name cannot be empty")

if __name__ == "__main__":
    m = Member("Bob")
    m.roles.append("editor")
    print(m)
    
    conf = Config(8080)
    print(f"Frozen Config: {conf}")
    # conf.port = 90 # Raises FrozenInstanceError if uncommented
