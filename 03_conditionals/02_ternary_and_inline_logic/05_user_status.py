"""
User Status logic.
"""

def format_user_status(is_active: bool, is_verified: bool, is_premium: bool) -> str:
    """
    Formats user status badge based on multiple conditions.
    
    Args:
        is_active: Whether user is active
        is_verified: Whether email is verified
        is_premium: Whether user has premium subscription
    
    Returns:
        Formatted status string
    
    Real-world use case: User dashboards, admin panels, reporting.
    """
    # Nested ternary (use sparingly for readability)
    status = ("✓ PREMIUM" if is_premium else "✓ VERIFIED") if is_verified else "⚠ UNVERIFIED"
    
    # Add active/inactive prefix
    final_status = f"ACTIVE - {status}" if is_active else f"INACTIVE - {status}"
    
    return final_status


def demonstrate_user_status() -> None:
    """
    Demonstrates complex status formatting using ternary logic.
    
    Real-world use case: User profile management.
    """
    users = [
        (True, True, True, "Active premium verified user"),
        (True, True, False, "Active verified standard user"),
        (True, False, False, "Active unverified user"),
        (False, True, True, "Inactive premium user"),
    ]
    
    for active, verified, premium, description in users:
        status = format_user_status(active, verified, premium)
        print(f"{status:30} | {description}")


if __name__ == "__main__":
    demonstrate_user_status()
