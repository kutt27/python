"""
Subscription Pricing Calculator logic.
"""

from enum import Enum

class PlanTier(Enum):
    """Subscription plan tiers."""
    FREE = "free"
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"


def calculate_pricing(tier: str, users: int, monthly: bool = True) -> float:
    """
    Calculates subscription pricing based on tier and user count.
    
    Args:
        tier: Subscription tier (free/basic/pro/enterprise)
        users: Number of users
        monthly: If True, monthly pricing; if False, annual pricing
    
    Returns:
        Price in dollars
    
    Real-world use case: SaaS pricing calculator, subscription management.
    """
    tier_lower = tier.lower()
    
    # Base pricing per user
    if tier_lower == "free":
        base_price = 0
    elif tier_lower == "basic":
        base_price = 10
    elif tier_lower == "pro":
        base_price = 25
    elif tier_lower == "enterprise":
        base_price = 50
    else:
        raise ValueError(f"Unknown tier: {tier}")
    
    # Calculate total
    total = base_price * users
    
    # Annual discount (20% off)
    if not monthly:
        total = total * 12 * 0.8  # 20% discount
    
    return total


def demonstrate_subscription_pricing() -> None:
    """
    Demonstrates subscription pricing calculation using if/elif/else.
    
    Real-world use case: SaaS pricing, tier-based billing.
    """
    tiers = ["free", "basic", "pro", "enterprise"]
    user_count = 10
    
    for tier in tiers:
        monthly_price = calculate_pricing(tier, user_count, monthly=True)
        annual_price = calculate_pricing(tier, user_count, monthly=False)
        
        print(f"\n{tier.upper()} tier ({user_count} users):")
        print(f"  Monthly: ${monthly_price:.2f}/month")
        print(f"  Annual: ${annual_price:.2f}/year (20% savings)")


if __name__ == "__main__":
    demonstrate_subscription_pricing()
