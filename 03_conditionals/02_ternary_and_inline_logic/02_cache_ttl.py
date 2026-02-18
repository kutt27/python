"""
Cache TTL logic.
"""

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


if __name__ == "__main__":
    demonstrate_cache_ttl()
