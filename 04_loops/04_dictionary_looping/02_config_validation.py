"""
Configuration Validation.
"""

from typing import Dict, List, Any, Tuple

def validate_config(config: Dict[str, Any], required_keys: List[str]) -> Tuple[bool, List[str]]:
    """
    Validates configuration has all required keys.
    
    Args:
        config: Configuration dictionary
        required_keys: List of required keys
    
    Returns:
        Tuple of (is_valid, missing_keys)
    
    Real-world use case: Application startup validation.
    """
    missing = []
    
    for key in required_keys:
        if key not in config:
            missing.append(key)
    
    return (len(missing) == 0, missing)


def demonstrate_config_validation() -> None:
    """
    Demonstrates configuration validation.
    """
    app_config = {
        "database_url": "postgresql://localhost/db",
        "api_key": "abc123",
        "debug": True
    }
    
    required = ["database_url", "api_key", "redis_url"]
    is_valid, missing = validate_config(app_config, required)
    
    print(f"Configuration valid: {is_valid}")
    if not is_valid:
        print(f"Missing keys: {missing}")


if __name__ == "__main__":
    demonstrate_config_validation()
