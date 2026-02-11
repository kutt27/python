"""
Demonstrates using tuples as dictionary keys (possible because tuples are hashable).
"""

def demonstrate_tuple_keys() -> None:
    # Cache mapping (endpoint, method) -> response
    api_cache = {
        ("/users", "GET"): "User list",
        ("/users", "POST"): "User created"
    }
    
    key = ("/users", "GET")
    print(f"Lookup for {key}: {api_cache.get(key)}")

if __name__ == "__main__":
    demonstrate_tuple_keys()
