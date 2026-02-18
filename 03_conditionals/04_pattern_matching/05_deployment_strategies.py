"""
Deployment Strategies logic.
"""

from typing import Dict, Any

def determine_deployment_strategy(config: Dict[str, Any]) -> str:
    """
    Determines deployment strategy based on configuration.
    
    Args:
        config: Deployment configuration
    
    Returns:
        Deployment strategy description
    
    Real-world use case: CI/CD pipeline configuration, deployment automation.
    """
    match config:
        # Blue-green deployment
        case {"strategy": "blue-green", "environment": env}:
            return f"🔵🟢 Blue-green deployment to {env}"
        
        # Canary deployment with percentage
        case {"strategy": "canary", "percentage": pct} if 0 < pct <= 100:
            return f"🐤 Canary deployment: {pct}% traffic"
        
        # Rolling deployment
        case {"strategy": "rolling", "batch_size": size}:
            return f"🔄 Rolling deployment: {size} instances at a time"
        
        # Feature flag deployment
        case {"strategy": "feature-flag", "flag": flag_name, "enabled": enabled}:
            status = "enabled" if enabled else "disabled"
            return f"🚩 Feature flag '{flag_name}' {status}"
        
        case _:
            return "📦 Standard deployment (all-at-once)"


def demonstrate_deployment_strategies() -> None:
    """
    Demonstrates strategy selection using structural matching.
    
    Real-world use case: CI/CD pipeline automation.
    """
    deployments = [
        {"strategy": "blue-green", "environment": "production"},
        {"strategy": "canary", "percentage": 10},
        {"strategy": "rolling", "batch_size": 3},
        {"strategy": "feature-flag", "flag": "new-ui", "enabled": True},
        {"strategy": "manual"},
    ]
    
    for config in deployments:
        strategy = determine_deployment_strategy(config)
        print(f"  {strategy}")


if __name__ == "__main__":
    demonstrate_deployment_strategies()
