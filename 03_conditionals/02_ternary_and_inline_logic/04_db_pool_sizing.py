"""
Database Pool Sizing logic.
"""

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


if __name__ == "__main__":
    demonstrate_db_pool_sizing()
