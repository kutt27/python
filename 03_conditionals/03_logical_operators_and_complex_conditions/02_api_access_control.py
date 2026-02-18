"""
API Access Control logic.
"""

from typing import List, Optional

def check_api_access(
    api_key: Optional[str],
    ip_address: str,
    rate_limit_exceeded: bool,
    allowed_ips: List[str]
) -> tuple[bool, str]:
    """
    Checks if API request should be allowed.
    
    Args:
        api_key: API key from request
        ip_address: Request IP address
        rate_limit_exceeded: Whether rate limit has been exceeded
        allowed_ips: List of allowed IP addresses
    
    Returns:
        Tuple of (is_allowed, reason)
    
    Real-world use case: API gateway, request authorization.
    """
    # Check authentication
    if not api_key or len(api_key) < 20:
        return (False, "Invalid or missing API key")
    
    # Check rate limiting
    if rate_limit_exceeded:
        return (False, "Rate limit exceeded")
    
    # Check IP allowlist (if configured)
    if allowed_ips and ip_address not in allowed_ips:
        return (False, f"IP {ip_address} not in allowlist")
    
    # All checks passed
    return (True, "Access granted")


def demonstrate_api_access() -> None:
    """
    Demonstrates API access control using complex boolean logic.
    
    Real-world use case: API gateways.
    """
    allowed_ips = ["192.168.1.10", "10.0.0.5"]
    
    api_tests = [
        ("abc123def456ghi789jkl", "192.168.1.10", False, "Valid request"),
        ("short_key", "192.168.1.10", False, "Invalid API key"),
        ("abc123def456ghi789jkl", "192.168.1.10", True, "Rate limited"),
        ("abc123def456ghi789jkl", "203.0.113.1", False, "Blocked IP"),
    ]
    
    for key, ip, rate_limited, description in api_tests:
        allowed, reason = check_api_access(key, ip, rate_limited, allowed_ips)
        status = "✓ ALLOW" if allowed else "✗ DENY"
        print(f"{status:10} | {description:20} | {reason}")


if __name__ == "__main__":
    demonstrate_api_access()
