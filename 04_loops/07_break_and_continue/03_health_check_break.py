"""
Health Check with break.
"""

from typing import List, Optional

def check_service_health(services: List[str]) -> tuple[bool, Optional[str]]:
    """
    Checks services health, stops on first failure (break pattern).
    
    Args:
        services: List of service names
    
    Returns:
        Tuple of (all_healthy, failed_service)
    
    Real-world use case: Health check monitoring, startup validation.
    """
    print(f"\nChecking health of {len(services)} services")
    print("-" * 60)
    
    for service in services:
        # Simulate health check
        is_healthy = "cache" not in service.lower()  # Simplified: cache service fails
        
        if is_healthy:
            print(f"  ✓ {service}: Healthy")
        else:
            print(f"  ✗ {service}: FAILED")
            return (False, service)  # Stop checking on first failure
    
    return (True, None)


def demonstrate_health_check() -> None:
    """
    Demonstrates health check with early exit on failure.
    """
    service_list = ["API", "Database", "Cache", "Queue"]
    all_healthy, failed = check_service_health(service_list)
    
    if all_healthy:
        print("\n✓ All services healthy")
    else:
        print(f"\n✗ Service failure detected: {failed}")


if __name__ == "__main__":
    demonstrate_health_check()
