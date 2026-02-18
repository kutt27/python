"""
Auto Scaling logic.
"""

def determine_auto_scale_action(
    cpu_usage: float,
    memory_usage: float,
    current_instances: int,
    min_instances: int = 2,
    max_instances: int = 10
) -> str:
    """
    Determines auto-scaling action based on resource usage.
    
    Args:
        cpu_usage: CPU usage percentage (0-100)
        memory_usage: Memory usage percentage (0-100)
        current_instances: Current number of running instances
        min_instances: Minimum allowed instances
        max_instances: Maximum allowed instances
    
    Returns:
        Action to take: "scale_up", "scale_down", or "no_change"
    
    Real-world use case: Auto-scaling, cost optimization.
    """
    # Scale up if resources are constrained
    if (cpu_usage > 80 or memory_usage > 85) and current_instances < max_instances:
        return "scale_up"
    
    # Scale down if underutilized
    if cpu_usage < 30 and memory_usage < 40 and current_instances > min_instances:
        return "scale_down"
    
    return "no_change"


def demonstrate_auto_scaling() -> None:
    """
    Demonstrates auto-scaling decisions based on resource usage.
    
    Real-world use case: Cloud infrastructure management.
    """
    scaling_scenarios = [
        (85, 90, 5, "High load"),
        (45, 50, 5, "Normal load"),
        (25, 35, 5, "Low load"),
        (90, 80, 10, "High load, at max instances"),
        (20, 30, 2, "Low load, at min instances"),
    ]
    
    for cpu, mem, instances, description in scaling_scenarios:
        action = determine_auto_scale_action(cpu, mem, instances)
        
        action_icon = {
            "scale_up": "⬆",
            "scale_down": "⬇",
            "no_change": "→"
        }[action]
        
        print(f"{action_icon} {action.upper():12} | CPU:{cpu:>3}% MEM:{mem:>3}% | {instances} instances | {description}")


if __name__ == "__main__":
    demonstrate_auto_scaling()
