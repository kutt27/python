"""
Demonstrates string encoding (str to bytes) and decoding (bytes to str).
"""

def demonstrate_encoding() -> None:
    product_name = "Café Spécial ☕"
    print(f"Original: {product_name}")
    
    # Encode to UTF-8
    encoded = product_name.encode("utf-8")
    print(f"Encoded (bytes): {encoded}")
    print(f"Byte length: {len(encoded)}")
    
    # Decode back
    decoded = encoded.decode("utf-8")
    print(f"Decoded: {decoded}")
    
    print("\nBest Practice: Use UTF-8 for international compatibility.")

if __name__ == "__main__":
    demonstrate_encoding()
