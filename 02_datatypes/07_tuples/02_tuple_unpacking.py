"""
Demonstrates tuple unpacking and extended unpacking with *.
"""

def demonstrate_unpacking() -> None:
    # Basic unpacking
    user_record = (101, "admin", "admin@example.com")
    user_id, username, email = user_record
    
    print(f"ID: {user_id}, User: {username}, Email: {email}")
    
    # Extended unpacking
    server_metrics = ("CPU", "70%", "Memory", "80%", "Disk", "50%")
    metric_name, *values = server_metrics
    
    print(f"\nMetric: {metric_name}")
    print(f"Values: {values}")

if __name__ == "__main__":
    demonstrate_unpacking()
