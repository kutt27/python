"""
Demonstrates using .get() for handling configuration with fallback values.
"""

def demonstrate_defaults() -> None:
    config = {"debug": True, "port": 8000}
    
    # Fallback if key is missing
    port = config.get("port", 3000)
    workers = config.get("workers", 4)
    
    print(f"Port: {port}")
    print(f"Workers: {workers} (Default)")

if __name__ == "__main__":
    demonstrate_defaults()
