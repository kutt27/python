"""
Demonstrates common string methods like strip(), lower(), split(), and join().
"""

def demonstrate_string_methods() -> None:
    # Cleaning input
    raw_email = "  Admin@Example.COM  "
    clean_email = raw_email.strip().lower()
    print(f"Cleaned email: '{clean_email}'")
    
    # Path processing
    path = "/api/v1/users/123/profile"
    parts = path.strip("/").split("/")
    print(f"Path parts: {parts}")
    
    # Joining
    reconstructed = "/" + "/".join(parts)
    print(f"Reconstructed: {reconstructed}")

if __name__ == "__main__":
    demonstrate_string_methods()
