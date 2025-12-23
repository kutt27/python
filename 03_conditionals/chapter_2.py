"""
Python Conditionals: Ternary Operator and Inline Logic
=======================================================

Topic: Ternary expressions, inline conditionals, and concise decision making

Real-World Applications:
- Configuration defaults and fallbacks
- Feature flag evaluation
- Conditional rendering in templates
- Dynamic resource allocation
- Quick validation and transformation
"""

from typing import Optional


def calculate_delivery_fee(order_amount: float, customer_tier: str = "standard") -> float:
    """
    Calculates delivery fee based on order amount and customer tier.
    
    Ternary operator provides concise conditional logic:
    value_if_true if condition else value_if_false
    
    Args:
        order_amount: Total order amount
        customer_tier: Customer membership tier
    
    Returns:
        Delivery fee amount
    
    Real-world use case: E-commerce checkout, logistics pricing.
    """
    # Free delivery threshold varies by tier
    free_threshold = 100 if customer_tier == "premium" else 200
    
    # Ternary operator for delivery fee calculation
    delivery_fee = 0 if order_amount >= free_threshold else 9.99
    
    return delivery_fee


def get_cache_ttl(is_static: bool, is_authenticated: bool = False) -> int:
    """
    Determines cache TTL (time-to-live) based on content type.
    
    Args:
        is_static: Whether content is static
        is_authenticated: Whether request is authenticated
    
    Returns:
        Cache TTL in seconds
    
    Real-world use case: CDN configuration, cache invalidation strategy.
    """
    # Static content cached longer
    # Authenticated content cached shorter or not at all
    ttl = (3600 if is_static else 300) if not is_authenticated else 0
    
    return ttl


def determine_log_level(is_production: bool, debug_mode: bool = False) -> str:
    """
    Determines appropriate log level for environment.
    
    Args:
        is_production: Whether running in production
        debug_mode: Whether debug mode is enabled
    
    Returns:
        Log level string
    
    Real-world use case: Logging configuration, observability setup.
    """
    if debug_mode:
        return "DEBUG"
    
    # Ternary for environment-based logging
    log_level = "WARNING" if is_production else "INFO"
    
    return log_level


def get_database_pool_size(environment: str, high_traffic: bool = False) -> int:
    """
    Determines database connection pool size.
    
    Args:
        environment: Environment name (dev/staging/production)
        high_traffic: Whether expecting high traffic
    
    Returns:
        Connection pool size
    
    Real-world use case: Database configuration, resource management.
    """
    # Base pool sizes
    base_sizes = {
        "development": 5,
        "staging": 10,
        "production": 20
    }
    
    base = base_sizes.get(environment, 5)
    
    # Double pool size for high traffic periods
    pool_size = base * 2 if high_traffic else base
    
    return pool_size


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


def determine_instance_type(cpu_intensive: bool, memory_intensive: bool) -> str:
    """
    Determines appropriate cloud instance type.
    
    Args:
        cpu_intensive: Whether workload is CPU-intensive
        memory_intensive: Whether workload is memory-intensive
    
    Returns:
        Instance type recommendation
    
    Real-world use case: Auto-scaling, resource provisioning.
    """
    if cpu_intensive and memory_intensive:
        return "c5.4xlarge"  # Compute + memory optimized
    elif cpu_intensive:
        return "c5.2xlarge"  # Compute optimized
    elif memory_intensive:
        return "r5.2xlarge"  # Memory optimized
    else:
        return "t3.medium"   # General purpose



def demonstrate_delivery_fees() -> None:
    """
    Demonstrates ternary operator usage for delivery fee calculation.
    
    Real-world use case: E-commerce logistics.
    """
    test_orders = [
        (50, "standard"),
        (150, "standard"),
        (50, "premium"),
        (150, "premium"),
    ]
    
    for amount, tier in test_orders:
        fee = calculate_delivery_fee(amount, tier)
        status = "FREE" if fee == 0 else f"${fee:.2f}"
        print(f"${amount:>6.2f} | {tier:8} tier | Delivery: {status}")


def demonstrate_cache_ttl() -> None:
    """
    Demonstrates nested ternary operators for cache configuration.
    
    Real-world use case: CDN/Caching logic.
    """
    scenarios = [
        (True, False, "Static content, public"),
        (False, False, "Dynamic content, public"),
        (True, True, "Static content, authenticated"),
        (False, True, "Dynamic content, authenticated"),
    ]
    
    for is_static, is_auth, description in scenarios:
        ttl = get_cache_ttl(is_static, is_auth)
        ttl_str = "No cache" if ttl == 0 else f"{ttl}s"
        print(f"{ttl_str:>10} | {description}")


def demonstrate_logging_levels() -> None:
    """
    Demonstrates environment-based logging level selection.
    
    Real-world use case: Application configuration.
    """
    configs = [
        (False, False, "Development, normal"),
        (True, False, "Production, normal"),
        (False, True, "Development, debug"),
        (True, True, "Production, debug"),
    ]
    
    for is_prod, debug, description in configs:
        level = determine_log_level(is_prod, debug)
        print(f"{level:8} | {description}")


def demonstrate_db_pool_sizing() -> None:
    """
    Demonstrates dynamic resource allocation based on conditions.
    
    Real-world use case: Database connection management.
    """
    environments = ["development", "staging", "production"]
    
    for env in environments:
        normal = get_database_pool_size(env, high_traffic=False)
        high = get_database_pool_size(env, high_traffic=True)
        print(f"{env.capitalize():12} | Normal: {normal:>2} | High traffic: {high:>2}")


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


def demonstrate_infrastructure_recommendations() -> None:
    """
    Demonstrates resource-based decision making for infrastructure.
    
    Real-world use case: Cloud resource provisioning.
    """
    workloads = [
        (True, True, "ML training (CPU + Memory)"),
        (True, False, "Video encoding (CPU)"),
        (False, True, "In-memory cache (Memory)"),
        (False, False, "Web server (General)"),
    ]
    
    for cpu, mem, description in workloads:
        instance = determine_instance_type(cpu, mem)
        print(f"{instance:12} | {description}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("TERNARY OPERATORS & INLINE CONDITIONALS".center(70))
    print("="*70)
    
    print("\n[1] DELIVERY FEE CALCULATOR")
    print("-" * 70)
    demonstrate_delivery_fees()
    
    print("\n\n[2] CACHE TTL CONFIGURATION")
    print("-" * 70)
    demonstrate_cache_ttl()
    
    print("\n\n[3] LOG LEVEL DETERMINATION")
    print("-" * 70)
    demonstrate_logging_levels()
    
    print("\n\n[4] DATABASE POOL SIZING")
    print("-" * 70)
    demonstrate_db_pool_sizing()
    
    print("\n\n[5] USER STATUS FORMATTING")
    print("-" * 70)
    demonstrate_user_status()
    
    print("\n\n[6] RATE LIMIT WARNINGS")
    print("-" * 70)
    demonstrate_rate_limit_warnings()
    
    print("\n\n[7] CLOUD INSTANCE RECOMMENDATIONS")
    print("-" * 70)
    demonstrate_infrastructure_recommendations()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Ternary: value_if_true if condition else value_if_false")
    print("2. Use for simple conditional assignments")
    print("3. Avoid nested ternaries - hurts readability")
    print("4. Perfect for default values and fallbacks")
    print("5. More concise than full if/else for simple cases")
    print("="*70)


if __name__ == "__main__":
    main()