"""
Log Level logic.
"""

def determine_log_level(is_production: bool, debug_mode: bool = False) -> str:
    """
    Determines appropriate log level for environment.
    
    Args:
        is_production: Whether running in production
        debug_mode: Whether debug mode is enabled
    
    Returns:
        Log level string
    
    Real-world use case: Logging configuration, observability setup.
    """
    if debug_mode:
        return "DEBUG"
    
    # Ternary for environment-based logging
    log_level = "WARNING" if is_production else "INFO"
    
    return log_level


def demonstrate_logging_levels() -> None:
    """
    Demonstrates environment-based logging level selection.
    
    Real-world use case: Application configuration.
    """
    configs = [
        (False, False, "Development, normal"),
        (True, False, "Production, normal"),
        (False, True, "Development, debug"),
        (True, True, "Production, debug"),
    ]
    
    for is_prod, debug, description in configs:
        level = determine_log_level(is_prod, debug)
        print(f"{level:8} | {description}")


if __name__ == "__main__":
    demonstrate_logging_levels()
