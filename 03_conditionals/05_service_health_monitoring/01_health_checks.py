"""
Health Checks logic.
"""

from enum import Enum

class ServiceStatus(Enum):
    """Service health status levels."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    OFFLINE = "offline"


def check_service_health(is_responding: bool, response_time_ms: float, error_rate: float) -> ServiceStatus:
    """
    Determines service health status based on metrics.
    
    Args:
        is_responding: Whether service is responding to requests
        response_time_ms: Average response time in milliseconds
        error_rate: Error rate as percentage (0-100)
    
    Returns:
        Service health status
    
    Real-world use case: Service monitoring, health dashboards.
    """
    if not is_responding:
        return ServiceStatus.OFFLINE
    
    # Service is responding, check if degraded
    if response_time_ms > 1000 or error_rate > 5.0:
        return ServiceStatus.DEGRADED
    
    return ServiceStatus.HEALTHY


def demonstrate_health_checks() -> None:
    """
    Demonstrates service health checks using metrics and thresholds.
    
    Real-world use case: Service monitoring, health dashboards.
    """
    services = [
        (True, 150, 2.0, "API Gateway"),
        (True, 850, 3.5, "Authentication Service"),
        (True, 1200, 1.0, "Database Service"),
        (True, 200, 8.0, "Payment Service"),
        (False, 0, 100.0, "Cache Service"),
    ]
    
    for responding, latency, errors, name in services:
        status = check_service_health(responding, latency, errors)
        icon = "✓" if status == ServiceStatus.HEALTHY else ("⚠" if status  == ServiceStatus.DEGRADED else "✗")
        
        print(f"{icon} {name:25} | {status.value.upper():8} | {latency:>6.0f}ms | {errors:>5.1f}% errors")


if __name__ == "__main__":
    demonstrate_health_checks()
