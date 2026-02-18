"""
Alert logic.
"""

from enum import Enum

class ServiceStatus(Enum):
    """Service health status levels."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    OFFLINE = "offline"

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


if __name__ == "__main__":
    demonstrate_alert_logic()
