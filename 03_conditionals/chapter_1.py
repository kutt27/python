"""
Python Conditionals: Pricing Engine Implementation
===================================================

Topic: if/elif/else statements, ternary operators, and conditional logic

Real-World Applications:
- E-commerce pricing engines
- Subscription tier management
- API rate limiting by plan
- Dynamic resource allocation
- Feature access control by user role
"""

from enum import Enum
from typing import Optional


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


def calculate_shipping_cost(order_total: float, is_premium: bool = False) -> float:
    """
    Calculates shipping cost with conditional logic.
    
    Args:
        order_total: Order subtotal
        is_premium: Whether customer has premium membership
    
    Returns:
        Shipping cost
    
    Real-world use case: E-commerce checkout, shipping calculations.
    """
    # Ternary operator for concise conditional
    shipping = 0 if (order_total > 50 or is_premium) else 5.99
    
    return shipping


def determine_discount(order_total: float, customer_type: str, promo_code: Optional[str] = None) -> float:
    """
    Determines discount percentage based on multiple conditions.
    
    Args:
        order_total: Order subtotal
        customer_type: Type of customer (new/returning/vip)
        promo_code: Optional promo code
    
    Returns:
        Discount percentage (0-100)
    
    Real-world use case: Promotional pricing, customer loyalty programs.
    """
    discount = 0.0
    
    # Base discount by customer type
    if customer_type == "vip":
        discount = 15.0
    elif customer_type == "returning":
        discount = 5.0
    elif customer_type == "new":
        discount = 10.0  # New customer incentive
    
    # Additional discount for large orders
    if order_total > 200:
        discount += 5.0
    elif order_total > 100:
        discount += 2.5
    
    # Promo code overrides (if better)
    if promo_code == "SAVE20":
        discount = max(discount, 20.0)
    elif promo_code == "FLASH30":
        discount = max(discount, 30.0)
    
    # Cap at 40%
    return min(discount, 40.0)


def check_access_permission(user_role: str, resource: str) -> bool:
    """
    Checks if user role has permission to access resource.
    
    Args:
        user_role: User's role (guest/user/admin/superadmin)
        resource: Resource being accessed
    
    Returns:
        True if access granted, False otherwise
    
    Real-world use case: Authorization systems, RBAC (Role-Based Access Control).
    """
    # Admin and superadmin have access to everything
    if user_role in ["admin", "superadmin"]:
        return True
    
    # Users can read and write
    if user_role == "user" and resource in ["read", "write"]:
        return True
    
    # Guests can only read
    if user_role == "guest" and resource == "read":
        return True
    
    # Default deny
    return False



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


def demonstrate_api_rate_limits() -> None:
    """
    Demonstrates API rate limit retrieval using pattern matching.
    
    Real-world use case: API gateway, rate limiting.
    """
    tiers = ["free", "basic", "pro", "enterprise"]
    for plan in tiers:
        limit = get_api_rate_limit(plan)
        print(f"{plan.capitalize():12} -> {limit:>8,} requests/hour")


def demonstrate_shipping_costs() -> None:
    """
    Demonstrates shipping cost calculation using ternary operators.
    
    Real-world use case: E-commerce checkout.
    """
    test_orders = [
        (30.00, False, "Regular customer, low order"),
        (75.00, False, "Regular customer, free shipping"),
        (25.00, True, "Premium customer, any order"),
    ]
    
    for total, is_premium, description in test_orders:
        cost = calculate_shipping_cost(total, is_premium)
        status = "FREE" if cost == 0 else f"${cost:.2f}"
        print(f"${total:6.2f} | {'Premium' if is_premium else 'Regular':8} | {status:>8} | {description}")


def demonstrate_dynamic_discounts() -> None:
    """
    Demonstrates complex discount logic with multiple conditions.
    
    Real-world use case: Promotional engines.
    """
    test_scenarios = [
        (50, "new", None),
        (150, "returning", None),
        (250, "vip", None),
        (80, "new", "SAVE20"),
        (300, "vip", "FLASH30"),
    ]
    
    for total, cust_type, promo in test_scenarios:
        discount = determine_discount(total, cust_type, promo)
        final_price = total * (1 - discount / 100)
        
        promo_str = f"+ {promo}" if promo else ""
        print(f"${total:>6.2f} | {cust_type:9} {promo_str:10} | {discount:>5.1f}% off | Final: ${final_price:.2f}")


def demonstrate_access_control() -> None:
    """
    Demonstrates role-based access control (RBAC).
    
    Real-world use case: Authorization systems.
    """
    roles = ["guest", "user", "admin", "superadmin"]
    resources = ["read", "write", "delete", "admin"]
    
    print(f"\n{'Role':12} | {'read':6} | {'write':6} | {'delete':6} | {'admin':6}")
    print("-" * 55)
    
    for role in roles:
        permissions = [check_access_permission(role, res) for res in resources]
        perm_str = " | ".join(["✓" if p else "✗" for p in permissions])
        print(f"{role:12} | {perm_str}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("CONDITIONALS: PRICING & ACCESS CONTROL".center(70))
    print("="*70)
    
    print("\n[1] SUBSCRIPTION PRICING CALCULATOR")
    print("-" * 70)
    demonstrate_subscription_pricing()
    
    print("\n\n[2] API RATE LIMITS")
    print("-" * 70)
    demonstrate_api_rate_limits()
    
    print("\n\n[3] SHIPPING COST CALCULATOR")
    print("-" * 70)
    demonstrate_shipping_costs()
    
    print("\n\n[4] DYNAMIC DISCOUNT CALCULATOR")
    print("-" * 70)
    demonstrate_dynamic_discounts()
    
    print("\n\n[5] ROLE-BASED ACCESS CONTROL")
    print("-" * 70)
    demonstrate_access_control()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. if/elif/else for multi-way branching")
    print("2. match/case (Python 3.10+) for pattern matching")
    print("3. Ternary operator: value_if_true if condition else value_if_false")
    print("4. Guard clauses (early return) make code more readable")
    print("5. Use comparison operators: ==, !=, <, >, <=, >=, in, not in")
    print("="*70)


if __name__ == "__main__":
    main()