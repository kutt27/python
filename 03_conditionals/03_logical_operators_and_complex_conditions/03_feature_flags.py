"""
Feature Flags logic.
"""

from typing import Optional, Dict, Any

def should_show_feature(
    user_role: str,
    feature_name: str,
    is_beta_user: bool = False,
    feature_flags: Optional[Dict[str, Any]] = None
) -> bool:
    """
    Determines if feature should be shown to user.
    
    Args:
        user_role: User's role (user/admin/superadmin)
        feature_name: Name of the feature
        is_beta_user: Whether user is in beta program
        feature_flags: Feature flag configuration
    
    Returns:
        True if feature should be shown
    
    Real-world use case: Feature toggles, A/B testing, gradual rollouts.
    """
    if feature_flags is None:
        feature_flags = {}
    
    # Admin and superadmin see all features
    if user_role in ["admin", "superadmin"]:
        return True
    
    # Beta features only for beta users
    if feature_name.startswith("beta_") and not is_beta_user:
        return False
    
    # Check feature flag configuration
    flag_config = feature_flags.get(feature_name, {})
    
    # Feature disabled globally
    if not flag_config.get("enabled", True):
        return False
    
    # Check role-specific access
    allowed_roles = flag_config.get("roles", ["user", "admin", "superadmin"])
    if user_role not in allowed_roles:
        return False
    
    return True


def demonstrate_feature_flags() -> None:
    """
    Demonstrates feature flag evaluation with role-based logic.
    
    Real-world use case: Gradual feature rollouts.
    """
    feature_flags = {
        "new_dashboard": {"enabled": True, "roles": ["admin", "superadmin"]},
        "beta_ai_chat": {"enabled": True, "roles": ["user", "admin"]},
        "legacy_reports": {"enabled": False},
    }
    
    test_features = [
        ("user", "new_dashboard", False, "New Dashboard"),
        ("admin", "new_dashboard", False, "New Dashboard"),
        ("user", "beta_ai_chat", True, "Beta AI Chat"),
        ("user", "beta_ai_chat", False, "Beta AI Chat"),
        ("user", "legacy_reports", False, "Legacy Reports"),
    ]
    
    for role, feature, is_beta, feature_desc in test_features:
        should_show = should_show_feature(role, feature, is_beta, feature_flags)
        status = "✓ SHOW" if should_show else "✗ HIDE"
        beta_str = " (beta user)" if is_beta else ""
        print(f"{status:10} | {role:10} | {feature_desc:20} {beta_str}")


if __name__ == "__main__":
    demonstrate_feature_flags()
