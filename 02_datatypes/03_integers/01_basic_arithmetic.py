"""
Demonstrates basic arithmetic operations with integers.
"""

def demonstrate_basic_arithmetic() -> None:
    cpu_cores_server1 = 16
    cpu_cores_server2 = 8
    
    # Addition
    total_cores = cpu_cores_server1 + cpu_cores_server2
    print(f"Total CPU cores: {total_cores}")
    
    # Subtraction
    reserved_cores = 10
    print(f"Available cores: {total_cores - reserved_cores}")
    
    # Division (always returns float)
    users = 1000
    servers = 4
    users_per_server = users / servers
    print(f"Average users per server: {users_per_server} (Type: {type(users_per_server)})")

if __name__ == "__main__":
    demonstrate_basic_arithmetic()
