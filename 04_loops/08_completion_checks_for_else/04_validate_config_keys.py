"""
Validate Configuration Keys.
"""

from typing import List, Dict

def validate_config_keys(config: Dict, required_keys: List[str]) -> bool:
    """
    Validates all required configuration keys exist.
    
    Args:
        config: Configuration dictionary
        required_keys: List of required keys
    
    Returns:
        True if all keys present, False otherwise
    
    Real-world use case: Application startup validation.
    """
    print(f"\nValidating configuration ({len(required_keys)} required keys)")
    print("-" * 60)
    
    for key in required_keys:
        print(f"  Checking '{key}'... ", end="")
        
        if key not in config:
            print(f"✗ MISSING")
            return False  # Early exit - validation failed
        else:
            print("✓ Found")
    
    else:
        # All keys validated successfully
        print("\n✅ ALL REQUIRED KEYS PRESENT")
        return True


def demonstrate_validation() -> None:
    """
    Demonstrates configuration key validation.
    """
    app_config = {
        "database_url": "postgres://localhost/db",
        "api_key": "abc123",
        "redis_url": "redis://localhost:6379"
    }
    
    required = ["database_url", "api_key", "redis_url"]
    is_valid = validate_config_keys(app_config, required)
    
    if is_valid:
        print("\n→ Starting application...")
    else:
        print("\n→ Cannot start - fix configuration and retry")


if __name__ == "__main__":
    demonstrate_validation()
