"""
Python Exceptions: Hierarchy & Catching Order
==============================================

Topic: Inheritance hierarchy and exception masking

Real-World Applications:
- Avoiding unreachable code blocks
- Catching specific errors before general ones
- Designing robust error handling logic
"""

class NetworkError(Exception):
    pass

class DNSLookupError(NetworkError):
    pass

class ConnectionTimeout(NetworkError):
    pass


def perform_network_op(error_type: str):
    """Simulate network operations raising different errors."""
    if error_type == "dns":
        raise DNSLookupError("Failed to resolve host")
    elif error_type == "timeout":
        raise ConnectionTimeout("Connection timed out after 30s")
    elif error_type == "generic":
        raise NetworkError("Unknown network failure")


def bad_catching_order(error_type: str):
    """
    Demonstrates INCORRECT order.
    The generic class catches everything, masking specific handlers.
    """
    print(f"\n[Bad Order] Testing: {error_type}")
    try:
        perform_network_op(error_type)
    except NetworkError:
        print("Caught by user generic: NetworkError (Too broad!)")
    except DNSLookupError:
        # unreachable code!
        print("Caught specific: DNSLookupError")  
    except ConnectionTimeout:
        # unreachable code!
        print("Caught specific: ConnectionTimeout")


def good_catching_order(error_type: str):
    """
    Demonstrates CORRECT order.
    Specific exceptions are caught first.
    """
    print(f"\n[Good Order] Testing: {error_type}")
    try:
        perform_network_op(error_type)
    except DNSLookupError as e:
        print(f"Caught specific: {type(e).__name__} -> Check DNS settings")
    except ConnectionTimeout as e:
        print(f"Caught specific: {type(e).__name__} -> Retry connection")
    except NetworkError as e:
        print(f"Caught generic: {type(e).__name__} -> General network check")


def main():
    """Demonstrates exception hierarchy and catching order."""
    print("="*70)
    print("EXCEPTION HIERARCHY & ORDER".center(70))
    print("="*70)
    
    print("\n--- Example 1: The Problem (Bad Order) ---")
    bad_catching_order("dns")
    # Result: Caught by generic, specific handler ignored.
    
    print("\n--- Example 2: The Solution (Good Order) ---")
    good_catching_order("dns")
    good_catching_order("timeout")
    good_catching_order("generic")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Python checks except blocks top-to-bottom")
    print("• A handler for a BaseClass will catch all SubClasses")
    print("• ALWAYS catch specific exceptions FIRST")
    print("• Catch generic Exception/BaseException LAST")
    print("="*70)


if __name__ == "__main__":
    main()