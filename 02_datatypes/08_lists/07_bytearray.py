"""
Demonstrates bytearray - a mutable sequence of bytes.
"""

def demonstrate_bytearray() -> None:
    packet = bytearray(b"HTTP")
    print(f"Initial: {packet}")
    
    packet.extend(b"/1.1")
    print(f"Extended: {packet}")
    
    # In-place replacement
    packet = packet.replace(b"HTTP", b"HTTPS")
    print(f"Modified: {packet}")
    
    print(f"Final as string: {packet.decode('utf-8')}")

if __name__ == "__main__":
    demonstrate_bytearray()
