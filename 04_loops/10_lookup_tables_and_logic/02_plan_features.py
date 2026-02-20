"""
Subscription Plan Features.
"""

from typing import List, Dict

def get_plan_features(plan_tier: str) -> List[str]:
    """
    Returns features available for subscription plan.
    
    Args:
        plan_tier: Plan tier name
    
    Returns:
        List of available features
    
    Real-world use case: SaaS feature gating, subscription management.
    """
    PLAN_FEATURES: Dict[str, List[str]] = {
        "free": ["basic_api", "email_support"],
        "basic": ["basic_api", "email_support", "analytics", "webhooks"],
        "pro": ["basic_api", "email_support", "analytics", "webhooks", 
                "priority_support", "advanced_analytics", "custom_domain"],
        "enterprise": ["basic_api", "email_support", "analytics", "webhooks",
                      "priority_support", "advanced_analytics", "custom_domain",
                      "dedicated_account_manager", "sla_guarantee", "custom_integration"]
    }
    
    return PLAN_FEATURES.get(plan_tier.lower(), [])


def demonstrate_plan_features() -> None:
    """
    Demonstrates plan feature lookup.
    """
    plans = ["free", "basic", "pro", "enterprise"]
    
    for plan in plans:
        features = get_plan_features(plan)
        print(f"\n{plan.upper()} Plan ({len(features)} features):")
        for feature in features:
            print(f"  ✓ {feature}")


if __name__ == "__main__":
    demonstrate_plan_features()
