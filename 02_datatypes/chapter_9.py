"""
Python Sets: Advanced Operations and Use Cases
===============================================

Topic: Set operations, mathematical set theory, and optimization

Real-World Applications:
- Deduplication in data pipelines
- Permission and role management
- Feature flag systems
- Tag and category management
- Database query optimization (JOIN operations)
"""

from typing import Set


def demonstrate_set_operations() -> None:
    """
    Demonstrates mathematical set operations.
    
    Sets support standard mathematical operations:
    - Union (|): All elements from both sets
    - Intersection (&): Common elements
    - Difference (-): Elements in first but not second
    - Symmetric difference (^): Elements in either but not both
    
    Real-world use case: Feature flag management, user permissions.
    """
    # Example: Microservices feature deployment
    production_features: Set[str] = {"auth", "search", "checkout", "analytics"}
    beta_features: Set[str] = {"checkout", "recommendations", "dark_mode", "ai_chat"}
    
    print(f"Production features: {production_features}")
    print(f"Beta features: {beta_features}")
    
    # Union: All features across both environments
    all_features = production_features | beta_features
    print(f"\nAll features (union): {all_features}")
    print(f"  Total unique features: {len(all_features)}")
    
    # Intersection: Features in both (already tested in production AND beta)
    tested_features = production_features & beta_features
    print(f"\nTested in both (intersection): {tested_features}")
    
    # Difference: Production-only features
    prod_only = production_features - beta_features
    print(f"\nProduction-only features: {prod_only}")
    
    # Symmetric difference: Features in either but not both
    exclusive_features = production_features ^ beta_features
    print(f"\nExclusive to one environment: {exclusive_features}")


def demonstrate_set_methods() -> None:
    """
    Demonstrates set methods for membership and comparison.
    
    Real-world use case: Permission validation, subset checking.
    """
    # Example: Role-based permissions
    admin_permissions: Set[str] = {"read", "write", "delete", "admin", "audit"}
    user_permissions: Set[str] = {"read", "write"}
    guest_permissions: Set[str] = {"read"}
    
    print(f"\nAdmin permissions: {admin_permissions}")
    print(f"User permissions: {user_permissions}")
    print(f"Guest permissions: {guest_permissions}")
    
    # Subset check: Are user permissions a subset of admin?
    is_subset = user_permissions.issubset(admin_permissions)
    print(f"\nUser ⊆ Admin? {is_subset}")
    
    # Superset check
    is_superset = admin_permissions.issuperset(user_permissions)
    print(f"Admin ⊇ User? {is_superset}")
    
    # Disjoint check: No common permissions
    premium_features: Set[str] = {"export_pdf", "api_access"}
    is_disjoint = guest_permissions.isdisjoint(premium_features)
    print(f"\nGuest ∩ Premium = ∅? {is_disjoint}")


def demonstrate_membership_testing() -> None:
    """
    Demonstrates O(1) membership testing - a key advantage of sets.
    
    Real-world use case: Validation, allowlists/blocklists, caching.
    """
    # Example: IP address allowlist
    allowed_ips: Set[str] = {
        "192.168.1.10",
        "192.168.1.20",
        "10.0.0.5",
        "172.16.0.100"
    }
    
    print(f"\nAllowed IPs: {len(allowed_ips)} addresses")
    
    # Fast membership test (O(1) average case)
    incoming_ip = "192.168.1.10"
    is_allowed = incoming_ip in allowed_ips
    
    print(f"\nIncoming connection from: {incoming_ip}")
    print(f"Access granted: {is_allowed}")
    
    # Blocked IP
    blocked_ip = "203.0.113.45"
    is_blocked = blocked_ip not in allowed_ips
    print(f"\nConnection from: {blocked_ip}")
    print(f"Is blocked: {is_blocked}")
    
    print(f"\n{'='*60}")
    print("Performance: Set membership testing is O(1)")
    print("  vs List membership testing which is O(n)")
    print("  For large datasets, sets are MUCH faster")
    print(f"{'='*60}")


def demonstrate_deduplication() -> None:
    """
    Demonstrates using sets for deduplication.
    
    Real-world use case: Removing duplicates from data pipelines, ETL.
    """
    # Example: User IDs from multiple data sources
    source_a_users = [101, 102, 103, 104, 105, 101, 102]  # Has duplicates
    source_b_users = [104, 105, 106, 107, 108, 104]       # Has duplicates
    
    print(f"\nSource A user IDs: {source_a_users}")
    print(f"  Count: {len(source_a_users)}")
    
    # Deduplicate using set
    unique_users_a = set(source_a_users)
    print(f"\nUnique users from A: {unique_users_a}")
    print(f"  Count: {len(unique_users_a)}")
    
    # Combine and deduplicate from both sources
    all_unique_users = set(source_a_users) | set(source_b_users)
    print(f"\nAll unique users: {sorted(all_unique_users)}")
    print(f"  Total unique: {len(all_unique_users)}")


def demonstrate_set_modifications() -> None:
    """
    Demonstrates modifying sets with add, update, remove, discard.
    
    Real-world use case: Dynamic tag management, active session tracking.
    """
    # Example: Tags for a blog post
    post_tags: Set[str] = {"python", "programming"}
    
    print(f"\nInitial tags: {post_tags}")
    
    # Add single tag
    post_tags.add("tutorial")
    print(f"After add: {post_tags}")
    
    # Update with multiple tags
    new_tags = {"backend", "webdev", "python"}  # python already exists
    post_tags.update(new_tags)
    print(f"After update: {post_tags}")
    
    # Remove (raises error if not found)
    post_tags.discard("webdev")  # Safe removal
    print(f"After discard: {post_tags}")
    
    # Clear all
    temp_tags = post_tags.copy()
    temp_tags.clear()
    print(f"\nAfter clear: {temp_tags}")
    print(f"Original intact: {post_tags}")


def find_common_interests(user1_interests: Set[str], user2_interests: Set[str]) -> Set[str]:
    """
    Finds common interests between two users.
    
    Args:
        user1_interests: First user's interests
        user2_interests: Second user's interests
    
    Returns:
        Set of common interests
    
    Real-world use case: Social network matching, recommendation systems.
    """
    return user1_interests & user2_interests


def get_unique_tags(tag_lists: list[Set[str]]) -> Set[str]:
    """
    Gets all unique tags across multiple collections.
    
    Args:
        tag_lists: List of tag sets
    
    Returns:
        Set of all unique tags
    
    Real-world use case: Content aggregation, taxonomy management.
    """
    all_tags: Set[str] = set()
    for tags in tag_lists:
        all_tags |= tags
    return all_tags


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON SETS: ADVANCED OPERATIONS".center(70))
    print("="*70)
    
    print("\n[1] SET OPERATIONS (Union, Intersection, Difference)")
    print("-" * 70)
    demonstrate_set_operations()
    
    print("\n\n[2] SET METHODS (Subset, Superset, Disjoint)")
    print("-" * 70)
    demonstrate_set_methods()
    
    print("\n\n[3] MEMBERSHIP TESTING (O(1) Performance)")
    print("-" * 70)
    demonstrate_membership_testing()
    
    print("\n\n[4] DEDUPLICATION")
    print("-" * 70)
    demonstrate_deduplication()
    
    print("\n\n[5] SET MODIFICATIONS")
    print("-" * 70)
    demonstrate_set_modifications()
    
    print("\n\n[6] PRACTICAL EXAMPLES")
    print("-" * 70)
    
    # Common interests
    alice_interests = {"python", "ml", "hiking", "photography"}
    bob_interests = {"python", "webdev", "photography", "gaming"}
    common = find_common_interests(alice_interests, bob_interests)
    print(f"\nAlice interests: {alice_interests}")
    print(f"Bob interests: {bob_interests}")
    print(f"Common interests: {common}")
    print(f"Match percentage: {len(common) / len(alice_interests | bob_interests) * 100:.1f}%")
    
    # Unique tags aggregation
    post1_tags = {"python", "tutorial", "beginner"}
    post2_tags = {"python", "advanced", "async"}
    post3_tags = {"javascript", "frontend", "tutorial"}
    
    all_tags = get_unique_tags([post1_tags, post2_tags, post3_tags])
    print(f"\nAggregated unique tags: {sorted(all_tags)}")
    print(f"Total unique tags: {len(all_tags)}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Sets provide O(1) membership testing (very fast)")
    print("2. Perfect for deduplication and uniqueness checking")
    print("3. Mathematical operations: | & - ^ for set algebra")
    print("4. Use sets when order doesn't matter but uniqueness does")
    print("5. Sets are mutable; frozenset for immutable version")
    print("="*70)


if __name__ == "__main__":
    main()
