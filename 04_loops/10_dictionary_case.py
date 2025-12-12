"""
Python Loops: Dictionary-Based Discount System
===============================================

Topic: Dictionary lookups for business logic, unpacking in loops

Real-World Applications:
- Coupon and discount systems
- Pricing tier management
- Feature entitlement lookup
- Tax calculation by region
- Subscription plan benefits
"""

from typing import Dict, List, Tuple


# Discount types: (percentage_discount, fixed_discount_amount)
DISCOUNT_TIERS: Dict[str, Tuple[float, float]] = {
    "VIP20": (0.20, 0),        # 20% percentage discount
    "FIXED50": (0, 50),        # $50 fixed discount
    "COMBO": (0.10, 25),       # 10% + $25
    "NEWUSER15": (0.15, 0),    # 15% for new users
    "BULK": (0.25, 0),         # 25% bulk discount
}


def calculate_discount(order_total: float, coupon_code: str) -> float:
    """
    Calculates  discount amount based on coupon code.
    
    Args:
        order_total: Order subtotal
        coupon_code: Discount coupon code
    
    Returns:
        Discount amount
    
    Real-world use case: E-commerce checkout, promotional pricing.
    """
    # Get discount values, default to no discount if code invalid
    percent_off, fixed_off = DISCOUNT_TIERS.get(coupon_code, (0, 0))
    
    # Calculate total discount
    discount = (order_total * percent_off) + fixed_off
    
    return min(discount, order_total)  # Can't discount more than order total


def process_orders_with_discounts(orders: List[Dict]) -> None:
    """
    Processes orders and applies discount codes.
    
    Args:
        orders: List of order dictionaries
    
    Real-world use case: Order processing pipeline, revenue calculation.
    """
    print("\nProcessing Orders with Discount Codes")
    print("="*70)
    print(f"{'Order ID':10} | {'Total':>8} | {'Coupon':10} | {'Discount':>10} | {'Final':>10}")
    print("-" * 70)
    
    total_revenue = 0
    total_discounts = 0
    
    for order in orders:
        order_id = order['id']
        subtotal = order['total']
        coupon = order.get('coupon', 'NONE')
        
        # Calculate discount using dictionary lookup
        discount = calculate_discount(subtotal, coupon)
        final_amount = subtotal - discount
        
        # Track totals
        total_revenue += final_amount
        total_discounts += discount
        
        print(f"{order_id:10} | ${subtotal:7.2f} | {coupon:10} | ${discount:>9.2f} | ${final_amount:>9.2f}")
    
    print("-" * 70)
    print(f"{'TOTALS':10} | {' ':8} | {' ':10} | ${total_discounts:>9.2f} | ${total_revenue:>9.2f}")
    
    print(f"\nRevenue Summary:")
    print(f"  Total Revenue: ${total_revenue:.2f}")
    print(f"  Total Discounts: ${total_discounts:.2f}")


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


def calculate_regional_tax(amount: float, region_code: str) -> float:
    """
    Calculates tax based on regional tax rates.
    
    Args:
        amount: Order amount
        region_code: Region/state code
    
    Returns:
        Tax amount
    
    Real-world use case: E-commerce tax calculation, compliance.
    """
    TAX_RATES: Dict[str, float] = {
        "CA": 0.0725,  # California: 7.25%
        "NY": 0.0400,  # New York: 4%
        "TX": 0.0625,  # Texas: 6.25%
        "FL": 0.06,    # Florida: 6%
        "WA": 0.065,   # Washington: 6.5%
    }
    
    tax_rate = TAX_RATES.get(region_code, 0)  # Default: no tax
    return amount * tax_rate


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("DICTIONARY-BASED BUSINESS LOGIC".center(70))
    print("="*70)
    
    print("\n[1] ORDER PROCESSING WITH DISCOUNTS")
    print("-" * 70)
    
    customer_orders = [
        {"id": "ORD-001", "total": 100.00, "coupon": "VIP20"},
        {"id": "ORD-002", "total": 250.00, "coupon": "FIXED50"},
        {"id": "ORD-003", "total": 150.00, "coupon": "COMBO"},
        {"id": "ORD-004", "total": 75.00, "coupon": "INVALID"},  # Invalid coupon
        {"id": "ORD-005", "total": 500.00, "coupon": "BULK"},
    ]
    
    process_orders_with_discounts(customer_orders)
    
    print("\n\n[2] SUBSCRIPTION PLAN FEATURES")
    print("-" * 70)
    
    plans = ["free", "basic", "pro", "enterprise"]
    
    for plan in plans:
        features = get_plan_features(plan)
        print(f"\n{plan.upper()} Plan ({len(features)} features):")
        for feature in features:
            print(f"  ✓ {feature}")
   
    print("\n\n[3] REGIONAL TAX CALCULATION")
    print("-" * 70)
    
    order_amount = 100.00
    regions = ["CA", "NY", "TX", "FL", "WA", "UNKNOWN"]
    
    print(f"\nTax calculation for ${order_amount:.2f} order:")
    print(f"{'Region':8} | {'Tax Rate':>10} | {'Tax Amount':>12} | {'Total':>10}")
    print("-" * 50)
    
    for region in regions:
        tax = calculate_regional_tax(order_amount, region)
        tax_rate = (tax / order_amount * 100) if tax > 0 else 0
        total = order_amount + tax
        
        print(f"{region:8} | {tax_rate:>9.2f}% | ${tax:>10.2f} | ${total:>9.2f}")
    
    print("\n\n[4] DISCOUNT TIER REFERENCE")
    print("-" * 70)
    
    print("\nAvailable Discount Codes:")
    print(f"{'Code':12} | {'% Off':>7} | {'$ Off':>7} | {'Description'}")
    print("-" * 60)
    
    descriptions = {
        "VIP20": "VIP members",
        "FIXED50": "Fixed $50 off",
        "COMBO": "Combo discount",
        "NEWUSER15": "New user promotion",
        "BULK": "Bulk order discount"
    }
    
    for code, (percent, fixed) in DISCOUNT_TIERS.items():
        percent_str = f"{percent*100:.0f}%" if percent > 0 else "-"
        fixed_str = f"${fixed:.0f}" if fixed > 0 else "-"
        desc = descriptions.get(code, "")
        
        print(f"{code:12} | {percent_str:>7} | {fixed_str:>7} | {desc}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Dictionaries ideal for lookup-based business logic")
    print("2. Use dict.get(key, default) to handle invalid keys gracefully")
    print("3. Tuple unpacking in loops: for key, value in dict.items()")
    print("4. Store configuration as constants (UPPER_CASE)")
    print("5. Better than long if/elif chains for many conditions")
    print("="*70)


if __name__ == "__main__":
    main()