"""
Python Sets: Mutable Collection Data Structure
===============================================

Topic: Understanding set mutability, in-place modifications, and object identity

Real-World Applications:
- Feature flag management in web applications
- User permission sets in authentication systems
- Deduplication in data processing pipelines
- Tag management in content management systems
"""

from typing import Set


def demonstrate_set_mutability() -> None:
    """
    Demonstrates that sets are MUTABLE - they can be modified in-place.
    
    Unlike immutable types (int, str, tuple), sets maintain the same identity
    when modified. This is crucial for understanding reference behavior.
    
    Real-world use case: Managing user permissions where you add/remove
    permissions without creating a new permissions object.
    """
    # Example: User permissions in an authentication system
    user_permissions: Set[str] = set()
    
    print(f"Initial permissions: {user_permissions}")
    print(f"Memory ID: {id(user_permissions)}")
    print(f"Type: {type(user_permissions)}\n")
    
    # Adding permissions (in-place modification)
    user_permissions.add("read")
    print(f"After adding 'read': {user_permissions}")
    print(f"Memory ID: {id(user_permissions)}  <- SAME object!")
    
    user_permissions.add("write")
    print(f"\nAfter adding 'write': {user_permissions}")
    print(f"Memory ID: {id(user_permissions)}  <- Still SAME object!")
    
    user_permissions.add("delete")
    print(f"\nAfter adding 'delete': {user_permissions}")
    print(f"Memory ID: {id(user_permissions)}  <- Still SAME object!")
    
    print(f"\n{'='*60}")
    print("IMPORTANT: Sets are MUTABLE")
    print("Adding elements modifies the SAME object in memory")
    print("The set's identity (memory address) never changes")
    print(f"{'='*60}")


def demonstrate_set_operations() -> None:
    """
    Demonstrates common set operations used in production systems.
    
    Sets are optimized for:
    - Membership testing (O(1) average case)
    - Removing duplicates
    - Mathematical set operations (union, intersection, difference)
    
    Real-world use case: Feature flags, user role management, tag systems.
    """
    # Example: Feature flags for A/B testing
    production_features: Set[str] = {"login", "search", "checkout"}
    beta_features: Set[str] = {"checkout", "recommendations", "dark_mode"}
    
    print(f"\nProduction features: {production_features}")
    print(f"Beta features: {beta_features}")
    
    # Union: All features across both environments
    all_features = production_features | beta_features
    print(f"\nAll features (union): {all_features}")
    
    # Intersection: Features in both environments
    common_features = production_features & beta_features
    print(f"Common features (intersection): {common_features}")
    
    # Difference: Features only in production
    prod_only = production_features - beta_features
    print(f"Production-only features: {prod_only}")
    
    # Symmetric difference: Features in either but not both
    exclusive_features = production_features ^ beta_features
    print(f"Exclusive features: {exclusive_features}")


def demonstrate_set_methods() -> None:
    """
    Demonstrates practical set methods for real-world scenarios.
    
    Common use cases:
    - add(): Add single element
    - update(): Add multiple elements
    - remove()/discard(): Remove elements
    - clear(): Remove all elements
    """
    # Example: Managing active user sessions
    active_sessions: Set[str] = set()
    
    print(f"\nInitial active sessions: {active_sessions}")
    
    # User logs in
    active_sessions.add("user_123")
    active_sessions.add("user_456")
    print(f"After logins: {active_sessions}")
    
    # Batch login (multiple users)
    new_logins = {"user_789", "user_101", "user_123"}  # user_123 already exists
    active_sessions.update(new_logins)
    print(f"After batch login: {active_sessions}")
    print(f"  Note: Duplicate 'user_123' was automatically ignored")
    
    # User logs out (safe removal)
    active_sessions.discard("user_456")  # Doesn't raise error if not found
    print(f"\nAfter logout (discard): {active_sessions}")
    
    # Check session count
    print(f"Total active sessions: {len(active_sessions)}")
    
    # Membership testing (O(1) performance)
    user_id = "user_789"
    is_active = user_id in active_sessions
    print(f"\nIs {user_id} logged in? {is_active}")


def demonstrate_frozenset() -> None:
    """
    Demonstrates frozenset - the immutable version of set.
    
    Use frozenset when you need:
    - Immutable set of values (can be used as dict keys)
    - Thread-safe set operations
    - Set members that are themselves sets
    
    Real-world use case: Permission templates, configuration constants.
    """
    # Example: Role-based permission templates
    ADMIN_PERMISSIONS = frozenset({"read", "write", "delete", "admin"})
    USER_PERMISSIONS = frozenset({"read", "write"})
    GUEST_PERMISSIONS = frozenset({"read"})
    
    print(f"\nPermission templates (immutable):")
    print(f"Admin: {ADMIN_PERMISSIONS}")
    print(f"User: {USER_PERMISSIONS}")
    print(f"Guest: {GUEST_PERMISSIONS}")
    
    # frozensets can be used as dictionary keys
    role_descriptions = {
        ADMIN_PERMISSIONS: "Full system access",
        USER_PERMISSIONS: "Standard user access",
        GUEST_PERMISSIONS: "Read-only access"
    }
    
    print(f"\nRole descriptions: {role_descriptions[USER_PERMISSIONS]}")
    
    # Attempting to modify raises AttributeError
    try:
        ADMIN_PERMISSIONS.add("super_admin")  # type: ignore
    except AttributeError as e:
        print(f"\n✗ Cannot modify frozenset: {e}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON SETS: MUTABLE COLLECTIONS".center(70))
    print("="*70)
    
    print("\n[1] SET MUTABILITY & IDENTITY")
    print("-" * 70)
    demonstrate_set_mutability()
    
    print("\n\n[2] SET OPERATIONS")
    print("-" * 70)
    demonstrate_set_operations()
    
    print("\n\n[3] PRACTICAL SET METHODS")
    print("-" * 70)
    demonstrate_set_methods()
    
    print("\n\n[4] FROZENSET (IMMUTABLE SETS)")
    print("-" * 70)
    demonstrate_frozenset()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Sets are mutable - they maintain identity when modified")
    print("2. Sets automatically handle duplicates (perfect for deduplication)")
    print("3. O(1) membership testing makes sets ideal for lookups")
    print("4. Use frozenset for immutable sets (can be dict keys)")
    print("5. Set operations (|, &, -, ^) are powerful for complex logic")
    print("="*70)


if __name__ == "__main__":
    main()