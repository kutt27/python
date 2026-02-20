"""
Incremental Resource Allocation.
"""

def allocate_resources_until_satisfied(
    required: int,
    pool_size: int
) -> tuple[bool, int]:
    """
    Allocates resources from pool incrementally.
    
    Args:
        required: Required resource units
        pool_size: Available resource units
    
    Returns:
        Tuple of (success, allocated)
    
    Real-world use case: Cloud resource allocation, load balancing.
    """
    allocated = 0
    increment = 10
    
    print(f"\nAllocating {required} units from pool of {pool_size}")
    print("-" * 60)
    
    while allocated < required and allocated + increment <= pool_size:
        allocated += increment
        print(f"  Allocated: {allocated}/{required} units")
    
    success = allocated >= required
    status = "✓ Satisfied" if success else "✗ Insufficient resources"
    print(f"\n{status}: Allocated {allocated} units")
    
    return (success, allocated)


def demonstrate_allocation() -> None:
    """
    Demonstrates resource allocation.
    """
    # Scenario 1: Successful allocation
    allocate_resources_until_satisfied(required=50, pool_size=100)
    
    # Scenario 2: Insufficient resources
    print()
    allocate_resources_until_satisfied(required=150, pool_size=100)


if __name__ == "__main__":
    demonstrate_allocation()
