"""
Rate Limit Warnigns logic.
"""

def get_rate_limit_message(remaining: int, limit: int) -> str:
    """
    Generates rate limit warning message.
    
    Args:
        remaining: Remaining requests
        limit: Total limit
    
    Returns:
        Warning message or empty string
    
    Real-world use case: API rate limiting notifications.
    """
    percentage_used = ((limit - remaining) / limit) * 100
    
    # Return warning if over 80% used
    message = (
        f"⚠ WARNING: {percentage_used:.0f}% of rate limit used ({remaining}/{limit} remaining)"
        if percentage_used >= 80
        else ""
    )
    
    return message


def demonstrate_rate_limit_warnings() -> None:
    """
    Demonstrates threshold-based warning message generation.
    
    Real-world use case: API usage monitoring.
    """
    limits = [
        (950, 1000),
        (500, 1000),
        (100, 1000),
    ]
    
    for remaining, limit in limits:
        message = get_rate_limit_message(remaining, limit)
        if message:
            print(message)
        else:
            print(f"✓ OK: {remaining}/{limit} requests remaining ({(remaining/limit)*100:.0f}%)")


if __name__ == "__main__":
    demonstrate_rate_limit_warnings()
