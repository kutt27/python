"""
API Rate Limit logic.
"""

def get_api_rate_limit(plan: str) -> int:
    """
    Returns API rate limit based on subscription plan.
    
    Args:
        plan: Subscription plan name
    
    Returns:
        Requests per hour allowed
    
    Real-world use case: API rate limiting, quota management.
    """
    match plan.lower():  # Python 3.10+ pattern matching
        case "free":
            return 100
        case "basic":
            return 1_000
        case "pro":
            return 10_000
        case "enterprise":
            return 100_000
        case _:
            return 100  # Default to free tier


def demonstrate_api_rate_limits() -> None:
    """
    Demonstrates API rate limit retrieval using pattern matching.
    
    Real-world use case: API gateway, rate limiting.
    """
    tiers = ["free", "basic", "pro", "enterprise"]
    for plan in tiers:
        limit = get_api_rate_limit(plan)
        print(f"{plan.capitalize():12} -> {limit:>8,} requests/hour")


if __name__ == "__main__":
    demonstrate_api_rate_limits()
