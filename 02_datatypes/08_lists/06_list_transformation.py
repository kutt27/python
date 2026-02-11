"""
Demonstrates basic list transformation (looping to create a new list).
"""

def demonstrate_transformation() -> None:
    log_entries = ["200 OK /users", "404 Not Found", "200 OK /health"]
    
    # Extract status codes
    status_codes = []
    for entry in log_entries:
        status_codes.append(entry.split()[0])
    
    print(f"Log entries: {log_entries}")
    print(f"Status codes: {status_codes}")

if __name__ == "__main__":
    demonstrate_transformation()
