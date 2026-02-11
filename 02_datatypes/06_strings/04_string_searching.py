"""
Demonstrates string searching and checking (in, find, startswith, endswith).
"""

def demonstrate_string_searching() -> None:
    log = "ERROR: Failed to connect to database at 127.0.0.1:5432"
    
    # Keyword search
    if "ERROR" in log:
        print("Error found in log")
    
    # Position search
    ip_start = log.find("127.")
    if ip_start != -1:
        print(f"IP address starts at index {ip_start}")
    
    # Prefix/Suffix check
    filename = "report.pdf"
    print(f"Is PDF? {filename.endswith('.pdf')}")
    print(f"Is temp? {filename.startswith('temp_')}")

if __name__ == "__main__":
    demonstrate_string_searching()
