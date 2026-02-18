"""
Infrastructure Recommendations logic.
"""

def determine_instance_type(cpu_intensive: bool, memory_intensive: bool) -> str:
    """
    Determines appropriate cloud instance type.
    
    Args:
        cpu_intensive: Whether workload is CPU-intensive
        memory_intensive: Whether workload is memory-intensive
    
    Returns:
        Instance type recommendation
    
    Real-world use case: Auto-scaling, resource provisioning.
    """
    if cpu_intensive and memory_intensive:
        return "c5.4xlarge"  # Compute + memory optimized
    elif cpu_intensive:
        return "c5.2xlarge"  # Compute optimized
    elif memory_intensive:
        return "r5.2xlarge"  # Memory optimized
    else:
        return "t3.medium"   # General purpose


def demonstrate_infrastructure_recommendations() -> None:
    """
    Demonstrates resource-based decision making for infrastructure.
    
    Real-world use case: Cloud resource provisioning.
    """
    workloads = [
        (True, True, "ML training (CPU + Memory)"),
        (True, False, "Video encoding (CPU)"),
        (False, True, "In-memory cache (Memory)"),
        (False, False, "Web server (General)"),
    ]
    
    for cpu, mem, description in workloads:
        instance = determine_instance_type(cpu, mem)
        print(f"{instance:12} | {description}")


if __name__ == "__main__":
    demonstrate_infrastructure_recommendations()
