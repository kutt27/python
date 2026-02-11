"""
Demonstrates useful integer methods and representations (bin, hex, oct, abs).
"""

def demonstrate_numeric_methods() -> None:
    status_code = 404
    
    print(f"Status Code: {status_code}")
    print(f"Bit length: {status_code.bit_length()}")
    print(f"Binary: {bin(status_code)}")
    print(f"Hexadecimal: {hex(status_code)}")
    print(f"Octal: {oct(status_code)}")
    
    error_delta = -42
    print(f"\nError delta: {error_delta}")
    print(f"Absolute error: {abs(error_delta)}")

if __name__ == "__main__":
    demonstrate_numeric_methods()
