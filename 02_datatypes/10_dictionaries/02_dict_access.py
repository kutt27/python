"""
Demonstrates accessing dictionary values safely.
"""

def demonstrate_access() -> None:
    db_config = {
        "host": "localhost",
        "port": 5432
    }
    
    # Direct access
    print(f"Host: {db_config['host']}")
    
    # Safe access with get()
    print(f"User (default): {db_config.get('user', 'guest')}")
    
    # Membership check
    print(f"Has Port? {'port' in db_config}")

if __name__ == "__main__":
    demonstrate_access()
