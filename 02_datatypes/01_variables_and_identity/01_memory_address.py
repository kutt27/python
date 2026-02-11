"""
Demonstrates how to check object memory addresses using id() and hex().
"""

def demonstrate_memory_address() -> None:
    # Configuration example: Database connection strings
    db_host_dev = "localhost"
    db_host_prod = "db.production.com"
    
    print(f"Development DB: {db_host_dev}")
    print(f"Memory ID: {id(db_host_dev)}")
    print(f"Hex address: {hex(id(db_host_dev))}")
    
    print(f"\nProduction DB: {db_host_prod}")
    print(f"Memory ID: {id(db_host_prod)}")
    print(f"Hex address: {hex(id(db_host_prod))}")
    
    # String interning for identical strings
    db_host_dev2 = "localhost"
    print("\nString interning demo:")
    print(f"db_host_dev is db_host_dev2: {db_host_dev is db_host_dev2}")
    print("Python interns (caches) short strings for memory efficiency")

if __name__ == "__main__":
    demonstrate_memory_address()
