"""
Circuit Breaker logic.
"""

from typing import Optional
from datetime import datetime, timedelta

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


if __name__ == "__main__":
    demonstrate_circuit_breaker()
