"""
Configuration Merging.
"""

from typing import Dict, Any

def merge_configurations(
    defaults: Dict[str, Any],
    overrides: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Merges configuration with overrides.
    
    Args:
        defaults: Default configuration
        overrides: Override values
    
    Returns:
        Merged configuration
    
    Real-world use case: Application config management.
    """
    merged = defaults.copy()
    
    for key, value in overrides.items():
        merged[key] = value
    
    return merged


def demonstrate_merging() -> None:
    """
    Demonstrates configuration merging.
    """
    default_config = {
        "theme": "light",
        "language": "en",
        "timeout": 30,
        "retries": 3
    }
    
    user_overrides = {
        "theme": "dark",
        "retries": 5
    }
    
    final_config = merge_configurations(default_config, user_overrides)
    
    print("\nDefault config:", default_config)
    print("User overrides:", user_overrides)
    print("\nFinal merged config:")
    for key, value in final_config.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    demonstrate_merging()
