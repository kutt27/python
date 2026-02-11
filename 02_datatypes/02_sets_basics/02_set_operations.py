"""
Demonstrates common set operations: union, intersection, difference, and symmetric difference.
"""

from typing import Set

def demonstrate_set_operations() -> None:
    # Example: Feature flags for A/B testing
    production_features: Set[str] = {"login", "search", "checkout"}
    beta_features: Set[str] = {"checkout", "recommendations", "dark_mode"}
    
    print(f"Production features: {production_features}")
    print(f"Beta features: {beta_features}")
    
    # Union: All features
    all_features = production_features | beta_features
    print(f"\nAll features (union): {all_features}")
    
    # Intersection: Common features
    common_features = production_features & beta_features
    print(f"Common features (intersection): {common_features}")
    
    # Difference: Features only in production
    prod_only = production_features - beta_features
    print(f"Production-only features: {prod_only}")
    
    # Symmetric difference: Features in either but not both
    exclusive_features = production_features ^ beta_features
    print(f"Exclusive features: {exclusive_features}")

if __name__ == "__main__":
    demonstrate_set_operations()
