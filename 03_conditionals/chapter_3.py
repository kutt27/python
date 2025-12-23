"""
Python Conditionals: Logical Operators and Complex Conditions
==============================================================

Topic: and, or, not operators with complex boolean expressions

Real-World Applications:
- User authentication and authorization
- Feature flag evaluation
- Input validation
- Access control systems
- Business rule engines
"""

from typing import List, Optional, Dict, Any


def validate_user_credentials(
    username: str,
    password: str,
    min_password_length: int = 8
) -> tuple[bool, str]:
    """
    Validates user credentials with multiple conditions.
    
    Args:
        username: User's username
        password: User's password
        min_password_length: Minimum required password length
    
    Returns:
        Tuple of (is_valid, message)
    
    Real-world use case: User registration, authentication systems.
    """
    # Multiple conditions with AND operator
    if not username or not password:
        return (False, "Username and password are required")
    
    if len(username) < 3 or len(password) < min_password_length:
        return (False, f"Username must be 3+ chars, password must be {min_password_length}+ chars")
    
    # Check for special characters (simplified)
    has_number = any(c.isdigit() for c in password)
    has_letter = any(c.isalpha() for c in password)
    
    if not (has_number and has_letter):
        return (False, "Password must contain both letters and numbers")
    
    return (True, "")


def check_api_access(
    api_key: Optional[str],
    ip_address: str,
    rate_limit_exceeded: bool,
    allowed_ips: List[str]
) -> tuple[bool, str]:
    """
    Checks if API request should be allowed.
    
    Args:
        api_key: API key from request
        ip_address: Request IP address
        rate_limit_exceeded: Whether rate limit has been exceeded
        allowed_ips: List of allowed IP addresses
    
    Returns:
        Tuple of (is_allowed, reason)
    
    Real-world use case: API gateway, request authorization.
    """
    # Check authentication
    if not api_key or len(api_key) < 20:
        return (False, "Invalid or missing API key")
    
    # Check rate limiting
    if rate_limit_exceeded:
        return (False, "Rate limit exceeded")
    
    # Check IP allowlist (if configured)
    if allowed_ips and ip_address not in allowed_ips:
        return (False, f"IP {ip_address} not in allowlist")
    
    # All checks passed
    return (True, "Access granted")


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


def evaluate_eligibility(
    age: int,
    has_license: bool,
    credit_score: int,
    employment_status: str
) -> tuple[bool, str]:
    """
    Evaluates eligibility for a service (e.g., car rental).
    
    Args:
        age: Applicant's age
        has_license: Whether applicant has valid license
        credit_score: Credit score (300-850)
        employment_status: Employment status
    
    Returns:
        Tuple of (is_eligible, reason)
    
    Real-world use case: Loan approval, service eligibility, risk assessment.
    """
    # Must meet basic requirements
    if age < 21:
        return (False, "Must be 21 or older")
    
    if not has_license:
        return (False, "Valid license required")
    
    # Credit and employment checks
    if credit_score < 600 and employment_status != "employed":
        return (False, "Insufficient credit score and not employed")
    
    # Either good credit OR employed can qualify
    if credit_score >= 650 or (credit_score >= 600 and employment_status == "employed"):
        return (True, "Eligible")
    
    return (False, "Does not meet credit/employment requirements")


def categorize_transaction(
    amount: float,
    is_international: bool,
    is_high_risk_merchant: bool,
    customer_category: str
) -> str:
    """
    Categorizes transaction for fraud detection.
    
    Args:
        amount: Transaction amount
        is_international: Whether transaction is international
        is_high_risk_merchant: Whether merchant is flagged as high-risk
        customer_category: Customer category (new/regular/vip)
    
    Returns:
        Risk category: "low", "medium", or "high"
    
    Real-world use case: Fraud detection, payment processing.
    """
    # High risk conditions
    if is_high_risk_merchant or (is_international and amount > 5000):
        return "high"
    
    # Medium risk conditions
    if (amount > 1000 and customer_category == "new") or is_international:
        return "medium"
    
    # VIP customers get lower risk scoring
    if customer_category == "vip":
        return "low"
    
    # Default based on amount
    return "medium" if amount > 500 else "low"



def demonstrate_credential_validation() -> None:
    """
    Demonstrates credential validation using logical operators.
    
    Real-world use case: User registration systems.
    """
    test_credentials = [
        ("admin", "Pass123", "Valid credentials"),
        ("ab", "Pass123", "Username too short"),
        ("admin", "short", "Password too short"),
        ("admin", "password", "Password missing number"),
    ]
    
    for username, password, description in test_credentials:
        is_valid, message = validate_user_credentials(username, password)
        status = "✓ VALID" if is_valid else "✗ INVALID"
        print(f"{status:10} | {description:30} | {message}")


def demonstrate_api_access() -> None:
    """
    Demonstrates API access control using complex boolean logic.
    
    Real-world use case: API gateways.
    """
    allowed_ips = ["192.168.1.10", "10.0.0.5"]
    
    api_tests = [
        ("abc123def456ghi789jkl", "192.168.1.10", False, "Valid request"),
        ("short_key", "192.168.1.10", False, "Invalid API key"),
        ("abc123def456ghi789jkl", "192.168.1.10", True, "Rate limited"),
        ("abc123def456ghi789jkl", "203.0.113.1", False, "Blocked IP"),
    ]
    
    for key, ip, rate_limited, description in api_tests:
        allowed, reason = check_api_access(key, ip, rate_limited, allowed_ips)
        status = "✓ ALLOW" if allowed else "✗ DENY"
        print(f"{status:10} | {description:20} | {reason}")


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


def demonstrate_eligibility() -> None:
    """
    Demonstrates eligibility evaluation using multiple criteria.
    
    Real-world use case: Loan/Service approval systems.
    """
    applicants = [
        (25, True, 700, "employed", "Good applicant"),
        (19, True, 750, "employed", "Too young"),
        (25, False, 750, "employed", "No license"),
        (25, True, 650, "unemployed", "Good credit"),
        (25, True, 550, "unemployed", "Low credit + not employed"),
    ]
    
    for age, license, credit, employment, description in applicants:
        eligible, reason = evaluate_eligibility(age, license, credit, employment)
        status = "✓ ELIGIBLE" if eligible else "✗ DENIED"
        print(f"{status:12} | {description:25} | {reason}")


def demonstrate_risk_analysis() -> None:
    """
    Demonstrates fraud risk categorization using logical AND/OR.
    
    Real-world use case: Payment processing.
    """
    transactions = [
        (100, False, False, "regular", "Small local purchase"),
        (2000, False, False, "new", "Large purchase, new customer"),
        (500, True, False, "vip", "International, VIP customer"),
        (1000, False, True, "regular", "High-risk merchant"),
        (6000, True, False, "regular", "Large international"),
    ]
    
    for amount, intl, high_risk, cust_cat, description in transactions:
        risk = categorize_transaction(amount, intl, high_risk, cust_cat)
        risk_icons = {"low": "🟢", "medium": "🟡", "high": "🔴"}
        
        print(f"{risk_icons[risk]} {risk.upper():6} | ${amount:>7.2f} | {description}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("LOGICAL OPERATORS & COMPLEX CONDITIONS".center(70))
    print("="*70)
    
    print("\n[1] USER CREDENTIAL VALIDATION")
    print("-" * 70)
    demonstrate_credential_validation()
    
    print("\n\n[2] API ACCESS CONTROL")
    print("-" * 70)
    demonstrate_api_access()
    
    print("\n\n[3] FEATURE FLAG EVALUATION")
    print("-" * 70)
    demonstrate_feature_flags()
    
    print("\n\n[4] ELIGIBILITY EVALUATION")
    print("-" * 70)
    demonstrate_eligibility()
    
    print("\n\n[5] TRANSACTION RISK CATEGORIZATION")
    print("-" * 70)
    demonstrate_risk_analysis()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. 'and' requires ALL conditions to be True")
    print("2. 'or' requires AT LEAST ONE condition to be True")
    print("3. 'not' inverts a boolean value")
    print("4. Use parentheses to control evaluation order")
    print("5. Short-circuit evaluation: 'and' stops at first False, 'or' at first True")
    print("="*70)


if __name__ == "__main__":
    main()