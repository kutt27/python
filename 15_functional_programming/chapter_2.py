"""
Functional Python: Immutability
================================

Topic: Immutable Data Structures

Concept:
Data should not be changed after creation. Instead of mutating objects,
create new objects with updated values.

Real-World Benefits:
- Thread safety (read-only is safe)
- No hidden state changes
- Predictable data flow
"""

from typing import NamedTuple, List, Tuple
from dataclasses import dataclass

# 1. Standard approach (Mutable - Dangerous in threaded/complex apps)
class MutableUser:
    def __init__(self, name: str, roles: List[str]):
        self.name = name
        self.roles = roles

# 2. Functional approach (Immutable)

# Option A: NamedTuple (Built-in, lightweight)
class UserNT(NamedTuple):
    name: str
    roles: Tuple[str, ...] # Tuple is immutable list

# Option B: Frozen Dataclass (Python 3.7+)
@dataclass(frozen=True)
class UserFrozen:
    name: str
    roles: Tuple[str, ...]
    
    def add_role(self, role: str) -> 'UserFrozen':
        """
        Returns a NEW instance with the added role.
        Does NOT modify self.
        """
        new_roles = self.roles + (role,)
        return UserFrozen(name=self.name, roles=new_roles)


def main():
    print("="*70)
    print("IMMUTABILITY".center(70))
    print("="*70)
    
    print("\n[1] The Problem with Mutability")
    m_user = MutableUser("Alice", ["admin"])
    ref_user = m_user # Aliasing
    ref_user.roles.append("super-admin") # Unexpected side effect
    print(f"Original User modified unexpectedly: {m_user.roles}")
    
    print("\n[2] NamedTuple (Immutable)")
    nt_user = UserNT("Bob", ("user",))
    print(f"Created: {nt_user}")
    try:
        # nt_user.name = "Robert" # AttributeError
        print("Tried to modify NamedTuple... Failed (Good!)")
    except AttributeError:
        print("✓ NamedTuple prevents modification")
        
    print("\n[3] Frozen Dataclass & Transformation")
    f_user = UserFrozen("Charlie", ("viewer",))
    print(f"Original: {f_user}")
    
    # "Change" the user by creating a new one
    f_user_v2 = f_user.add_role("editor")
    
    print(f"New V2:   {f_user_v2}")
    print(f"Original: {f_user} (Still intact!)")
    
    print(f"Same object? {f_user is f_user_v2}")
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Use `files/tuples` instead of `lists`")
    print("• Use `NamedTuple` or `@dataclass(frozen=True)`")
    print("• Treat data as 'Fact' - facts don't change, new facts are created")
    print("="*70)


if __name__ == "__main__":
    main()
