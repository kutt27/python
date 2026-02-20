"""
Environment Variable Generation.
"""

from typing import Dict, List

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


def demonstrate_env_vars() -> None:
    """
    Demonstrates environment variable generation.
    """
    env_config = {
        "db_host": "localhost",
        "db_port": "5432",
        "api_timeout": "30"
    }
    
    env_exports = generate_environment_vars(env_config)
    print("\nGenerated environment variables:")
    for export in env_exports:
        print(f"  {export}")


if __name__ == "__main__":
    demonstrate_env_vars()
