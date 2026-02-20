"""
Allocate Cloud Instance.
"""

from typing import List, Optional, Dict

def allocate_instance(required_memory: int, available_instances: List[Dict]) -> Optional[str]:
    """
    Allocates cloud instance with sufficient resources.
    
    Args:
        required_memory: Required memory in GB
        available_instances: List of instance dictionaries
    
    Returns:
        Instance ID if allocated, None otherwise
    
    Real-world use case: Cloud resource allocation, auto-scaling.
    """
    print(f"\nAllocating instance with {required_memory}GB memory")
    print("-" * 60)
    
    for instance in available_instances:
        instance_id = instance['id']
        memory = instance['memory_gb']
        
        print(f"  Instance {instance_id} ({memory}GB)... ", end="")
        
        if memory >= required_memory:
            print("✓ ALLOCATED")
            return instance_id
        else:
            print("✗ Insufficient memory")
    
    else:
        print("\n⚠ NO SUITABLE INSTANCE FOUND - Need to scale up")
        return None


def demonstrate_allocation() -> None:
    """
    Demonstrates instance allocation.
    """
    instances = [
        {"id": "i-001", "memory_gb": 4},
        {"id": "i-002", "memory_gb": 8},
        {"id": "i-003", "memory_gb": 16},
    ]
    
    allocated = allocate_instance(required_memory=12, available_instances=instances)
    
    if allocated:
        print(f"\n→ Using instance: {allocated}")
    else:
        print("\n→ Triggering auto-scaling to create larger instance")


if __name__ == "__main__":
    demonstrate_allocation()
