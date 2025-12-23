"""
Python Conditionals: Service Health Monitoring
===============================================

Topic: Boolean conditions, status checking, and alerting logic

Real-World Applications:
- Service health checks and monitoring
- Circuit breaker patterns
- Alerting and notification systems
- Automated remediation triggers
- SLA compliance checking
"""

from enum import Enum
from typing import Dict, List, Optional
from datetime import datetime, timedelta


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


def should_trigger_alert(
    status: ServiceStatus,
    duration_minutes: int,
    previous_alerts: int = 0
) -> bool:
    """
    Determines if an alert should be triggered.
    
    Args:
        status: Current service status
        duration_minutes: How long service has been in this status
        previous_alerts: Number of alerts already sent
    
    Returns:
        True if alert should be triggered
    
    Real-world use case: Alert fatigue prevention, notification throttling.
    """
    # Always alert on offline
    if status == ServiceStatus.OFFLINE:
        # But don't spam - only alert every 15 minutes
        return previous_alerts == 0 or duration_minutes % 15 == 0
    
    # Alert on degraded if it persists for 5+ minutes
    if status == ServiceStatus.DEGRADED:
        return duration_minutes >= 5 and previous_alerts == 0
    
    # No alert for healthy
    return False


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


def check_circuit_breaker(
    consecutive_failures: int,
    failure_threshold: int = 5,
    is_open: bool = False,
    last_failure_time: Optional[datetime] = None
) -> tuple[bool, str]:
    """
    Implements circuit breaker pattern logic.
    
    Args:
        consecutive_failures: Number of consecutive failures
        failure_threshold: Threshold to open circuit
        is_open: Whether circuit is currently open
        last_failure_time: When last failure occurred
    
    Returns:
        Tuple of (circuit_open, state)
    
    Real-world use case: Preventing cascading failures in microservices.
    """
    # If circuit is open, check if we should try again (half-open)
    if is_open and last_failure_time:
        time_since_failure = datetime.now() - last_failure_time
        if time_since_failure > timedelta(seconds=30):
            return (False, "half_open")  # Try again
        return (True, "open")  # Stay open
    
    # Check if we should open the circuit
    if consecutive_failures >= failure_threshold:
        return (True, "open")
    
    return (False, "closed")



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


def demonstrate_alert_logic() -> None:
    """
    Demonstrates alert triggering logic with throttling.
    
    Real-world use case: Incident management, notification systems.
    """
    alert_scenarios = [
        (ServiceStatus.OFFLINE, 1, 0, "Service just went offline"),
        (ServiceStatus.OFFLINE, 15, 1, "Still offline after 15 min"),
        (ServiceStatus.DEGRADED, 2, 0, "Recently degraded"),
        (ServiceStatus.DEGRADED, 6, 0, "Degraded for 6 minutes"),
        (ServiceStatus.HEALTHY, 10, 0, "Service is healthy"),
    ]
    
    for status, duration, prev_alerts, description in alert_scenarios:
        should_alert = should_trigger_alert(status, duration, prev_alerts)
        alert_status = "🔔 ALERT" if should_alert else "  No alert"
        
        print(f"{alert_status} | {status.value.upper():8} | {duration:>2}min | {description}")


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


def demonstrate_circuit_breaker() -> None:
    """
    Demonstrates the circuit breaker pattern for fault tolerance.
    
    Real-world use case: Resilience in microservices.
    """
    print("\nCircuit States:")
    
    # Closed -> Open
    failures = 0
    for i in range(6):
        failures += 1
        is_open, state = check_circuit_breaker(failures, failure_threshold=5)
        status_icon = "✗" if is_open else "✓"
        print(f"  Failure {failures}: {status_icon} Circuit {state.upper():10} {' <- Threshold reached!' if  failures == 5 else ''}")
    
    # Open -> Half-open (after timeout)
    last_fail = datetime.now() - timedelta(seconds=35)
    is_open, state = check_circuit_breaker(5, is_open=True, last_failure_time=last_fail)
    print(f"\n  After 35s timeout: Circuit {state.upper()} (trying request)")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("SERVICE HEALTH MONITORING & AUTOMATION".center(70))
    print("="*70)
    
    print("\n[1] SERVICE HEALTH CHECKS")
    print("-" * 70)
    demonstrate_health_checks()
    
    print("\n\n[2] ALERT TRIGGERING LOGIC")
    print("-" * 70)
    demonstrate_alert_logic()
    
    print("\n\n[3] AUTO-SCALING DECISIONS")
    print("-" * 70)
    demonstrate_auto_scaling()
    
    print("\n\n[4] CIRCUIT BREAKER PATTERN")
    print("-" * 70)
    demonstrate_circuit_breaker()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Use booleans for service status and health checks")
    print("2. Combine multiple conditions for complex decision-making")
    print("3. Circuit breakers prevent cascading failures")
    print("4. Auto-scaling based on metrics improves reliability")
    print("5. Alert throttling prevents notification fatigue")
    print("="*70)


if __name__ == "__main__":
    main()