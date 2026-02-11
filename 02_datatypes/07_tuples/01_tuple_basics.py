"""
Demonstrates tuple creation and immutability.
"""

def demonstrate_tuple_basics() -> None:
    # HTTP status tuple (code, message)
    http_response = (200, "OK")
    
    print(f"HTTP Response: {http_response}")
    print(f"Status Code: {http_response[0]}")
    print(f"Message: {http_response[1]}")
    
    # Tuples are immutable
    try:
        http_response[0] = 404  # type: ignore
    except TypeError as e:
        print(f"\nExpected error: {e}")

if __name__ == "__main__":
    demonstrate_tuple_basics()
