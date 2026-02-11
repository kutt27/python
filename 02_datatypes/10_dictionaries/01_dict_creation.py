"""
Demonstrates various ways to create dictionaries.
"""

def demonstrate_creation() -> None:
    # dict() constructor
    api_res = dict(status=200, msg="Success")
    print(f"Constructor: {api_res}")
    
    # Literal syntax (preferred)
    config = {
        "theme": "dark",
        "lang": "en"
    }
    print(f"Literal: {config}")
    
    # Empty dict
    cache = {}
    print(f"Empty: {cache} (Type: {type(cache)})")

if __name__ == "__main__":
    demonstrate_creation()
