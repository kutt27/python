"""
Python Dictionary Iteration
============================

Topic: Iterating over dictionaries - keys, values, items

Real-World Applications:
- Configuration file processing
- API response parsing
- Database record transformation
- Cache management
- Feature flag evaluation
"""

from typing import Dict, List, Any


def process_api_response(response: Dict[str, Any]) -> None:
    """
    Processes API response by iterating through fields.
    
    Args:
        response: API response dictionary
    
    Real-world use case: API integration, response validation.
    """
    print("\nProcessing API Response:")
    print("-" * 60)
    
    # Iterate over items (key-value pairs)
    for field, value in response.items():
        print(f"  {field}: {value}")


def validate_config(config: Dict[str, Any], required_keys: List[str]) -> tuple[bool, List[str]]:
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


def generate_environment_vars(config: Dict[str, str]) -> List[str]:
    """
    Generates environment variable exports from config.
    
    Args:
        config: Configuration dictionary
    
    Returns:
        List of export statements
    
    Real-world use case: Docker env files, shell scripts.
    """
    env_vars = []
    
    for key, value in config.items():
        export_statement = f"export {key.upper()}={value}"
        env_vars.append(export_statement)
    
    return env_vars


def count_status_codes(access_logs: List[Dict[str, Any]]) -> Dict[int, int]:
    """
    Counts HTTP status codes from access logs.
    
    Args:
        access_logs: List of access log entries
    
    Returns:
        Dictionary of status code counts
    
    Real-world use case: Web server analytics.
    """
    status_counts: Dict[int, int] = {}
    
    for log_entry in access_logs:
        status = log_entry.get("status", 0)
        status_counts[status] = status_counts.get(status, 0) + 1
    
    return status_counts


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


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("DICTIONARY ITERATION".center(70))
    print("="*70)
    
    print("\n[1] API RESPONSE PROCESSING")
    print("-" * 70)
    
    api_response = {
        "status": "success",
        "code": 200,
        "data": {"users": 42},
        "timestamp": "2024-12-05T10:00:00Z"
    }
    
    process_api_response(api_response)
    
    print("\n\n[2] CONFIGURATION VALIDATION")
    print("-" * 70)
    
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
    
    print("\n\n[3] ENVIRONMENT VARIABLE GENERATION")
    print("-" * 70)
    
    env_config = {
        "db_host": "localhost",
        "db_port": "5432",
        "api_timeout": "30"
    }
    
    env_exports = generate_environment_vars(env_config)
    print("\nGenerated environment variables:")
    for export in env_exports:
        print(f"  {export}")
    
    print("\n\n[4] STATUS CODE ANALYTICS")
    print("-" * 70)
    
    logs = [
        {"path": "/users", "status": 200},
        {"path": "/products", "status": 200},
        {"path": "/missing", "status": 404},
        {"path": "/api/data", "status": 500},
        {"path": "/health", "status": 200},
    ]
    
    status_summary = count_status_codes(logs)
    print("\nHTTP Status Code Summary:")
    for status, count in sorted(status_summary.items()):
        print(f"  {status}: {count} requests")
    
    print("\n\n[5] CONFIGURATION MERGING")
    print("-" * 70)
    
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
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. dict.items() - iterate over (key, value) pairs")
    print("2. dict.keys() - iterate over keys only")
    print("3. dict.values() - iterate over values only")
    print("4. for key in dict: also iterates over keys (default)") 
    print("5. Dictionaries maintain insertion order (Python 3.7+)")
    print("="*70)


if __name__ == "__main__":
    main()