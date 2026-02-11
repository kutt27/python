"""
Demonstrates basic string operations and f-string formatting.
"""

def demonstrate_string_basics() -> None:
    username = "admin_user"
    api_endpoint = "/api/v1/users"
    
    # f-string formatting
    log = f"User {username} accessed {api_endpoint}"
    print(f"Log: {log}")
    
    # Concatenation and repetition
    print(f"Path: {'/home' + '/user'}")
    print(f"Separator: {'-' * 10}")

if __name__ == "__main__":
    demonstrate_string_basics()
