"""
Python Conditionals: User Authentication Flow
==============================================

Topic: Complex conditional logic for authentication and session management

Real-World Applications:
- User login flows
- Multi-factor authentication
- Session management
- Password reset workflows
- Account lockout policies
"""

from typing import Optional, tuple, List
from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class UserSession:
    """User session data."""
    user_id: int
    username: str
    login_time: datetime
    expires_at: datetime
    is_mfa_verified: bool = False


def authenticate_user(
    username: str,
    password: str,
    stored_hash: str,
    account_locked: bool = False,
    failed_attempts: int = 0
) -> tuple[bool, str, Optional[UserSession]]:
    """
    Authenticates user with complex conditional logic.
    
    Args:
        username: User's username
        password: Provided password
        stored_hash: Stored password hash
        account_locked: Whether account is locked
        failed_attempts: Number of recent failed login attempts
    
    Returns:
        Tuple of (success, message, session)
    
    Real-world use case: User authentication, security systems.
    """
    # Check if account is locked
    if account_locked:
        return (False, "Account is locked due to too many failed attempts", None)
    
    # Check if approaching lockout threshold
    if failed_attempts >= 4:
        return (False, f"Warning: Account will be locked after {5 - failed_attempts} more failed attempt(s)", None)
    
    # Empty credentials
    if not username or not password:
        return (False, "Username and password are required", None)
    
    # Simulate password verification (in reality, use bcrypt/argon2)
    is_valid = password == stored_hash  # Simplified for demo
    
    if not is_valid:
        return (False, "Invalid credentials", None)
    
    # Create session
    now = datetime.now()
    session = UserSession(
        user_id=1,
        username=username,
        login_time=now,
        expires_at=now + timedelta(hours=24)
    )
    
    return (True, "Authentication successful - MFA required", session)


def verify_mfa_code(
    session: Optional[UserSession],
    mfa_code: str,
    expected_code: str
) -> tuple[bool, str]:
    """
    Verifies multi-factor authentication code.
    
    Args:
        session: Current user session
        mfa_code: MFA code provided by user
        expected_code: Expected MFA code
    
    Returns:
        Tuple of (success, message)
    
    Real-world use case: Two-factor authentication, security verification.
    """
    # Check if session exists
    if not session:
        return (False, "No active session found")
    
    # Check if already verified
    if session.is_mfa_verified:
        return (True, "MFA already verified for this session")
    
    # Check if session expired
    if datetime.now() > session.expires_at:
        return (False, "Session expired - please log in again")
    
    # Verify code
    if mfa_code != expected_code:
        return (False, "Invalid MFA code")
    
    # Success
    session.is_mfa_verified = True
    return (True, "MFA verification successful")


def check_session_validity(session: Optional[UserSession], require_mfa: bool = True) -> tuple[bool, str]:
    """
    Checks if session is valid for protected operations.
    
    Args:
        session: User session to validate
        require_mfa: Whether MFA verification is required
    
    Returns:
        Tuple of (is_valid, message)
    
    Real-world use case: Protected resource access, API authorization.
    """
    # No session
    if not session:
        return (False, "Not authenticated")
    
    # Session expired
    if datetime.now() > session.expires_at:
        return (False, "Session expired")
    
    # MFA required but not verified
    if require_mfa and not session.is_mfa_verified:
        return (False, "MFA verification required")
    
    # All checks passed
    return (True, "Session valid")


def determine_password_strength(password: str) -> tuple[str, List[str]]:
    """
    Determines password strength and provides feedback.
    
    Args:
        password: Password to evaluate
    
    Returns:
        Tuple of (strength_level, suggestions)
    
    Real-world use case: Password policies, user registration.
    """
    suggestions = []
    score = 0
    
    # Length check
    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
    
    # Character variety checks
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    if not has_lower:
        suggestions.append("Add lowercase letters")
    else:
        score += 1
    
    if not has_upper:
        suggestions.append("Add uppercase letters")
    else:
        score += 1
    
    if not has_digit:
        suggestions.append("Add numbers")
    else:
        score += 1
    
    if not has_special:
        suggestions.append("Add special characters (!@#$%)")
    else:
        score += 2
    
    # Determine strength level
    if score >= 7:
        strength = "strong"
    elif score >= 4:
        strength = "medium"
    else:
        strength = "weak"
    
    return (strength, suggestions)


def demonstrate_authentication() -> None:
    """
    Demonstrates the user authentication process with various scenarios.
    
    Real-world use case: Login systems, security filters.
    """
    auth_scenarios = [
        ("admin", "correct_password", "correct_password", False, 0, "Valid login"),
        ("admin", "wrong_password", "correct_password", False, 0, "Wrong password"),
        ("admin", "password", "password", False, 4, "Approaching lockout"),
        ("admin", "password", "password", True, 5, "Account locked"),
        ("", "", "password", False, 0, "Empty credentials"),
    ]
    
    for username, password, stored, locked, attempts, description in auth_scenarios:
        success, message, session = authenticate_user(
            username, password, stored, locked, attempts
        )
        status = "✓" if success else "✗"
        print(f"{status} {description:25} | {message}")


def demonstrate_mfa_verification() -> None:
    """
    Demonstrates multi-factor authentication verification logic.
    
    Real-world use case: 2FA, identity verification.
    """
    # Create a test session
    test_session = UserSession(
        user_id=1,
        username="admin",
        login_time=datetime.now(),
        expires_at=datetime.now() + timedelta(hours=24)
    )
    
    mfa_scenarios = [
        (test_session, "123456", "123456", "Correct MFA code"),
        (test_session, "000000", "123456", "Incorrect MFA code"),
        (None, "123456", "123456", "No session"),
    ]
    
    for session, code, expected, description in mfa_scenarios:
        success, message = verify_mfa_code(session, code, expected)
        status = "✓" if success else "✗"
        print(f"{status} {description:25} | {message}")


def demonstrate_session_validation() -> None:
    """
    Demonstrates session lifecycle and validity checking.
    
    Real-world use case: Session management, stateless APIs.
    """
    # Sessions for testing
    valid_session = UserSession(
        user_id=1,
        username="admin",
        login_time=datetime.now(),
        expires_at=datetime.now() + timedelta(hours=24),
        is_mfa_verified=True
    )
    
    no_mfa_session = UserSession(
        user_id=2,
        username="user",
        login_time=datetime.now(),
        expires_at=datetime.now() + timedelta(hours=24),
        is_mfa_verified=False
    )
    
    expired_session = UserSession(
        user_id=3,
        username="old_user",
        login_time=datetime.now() - timedelta(days=2),
        expires_at=datetime.now() - timedelta(days=1),
        is_mfa_verified=True
    )
    
    session_tests = [
        (valid_session, True, "Valid session with MFA"),
        (no_mfa_session, True, "Session without MFA"),
        (no_mfa_session, False, "Session, MFA not required"),
        (expired_session, True, "Expired session"),
        (None, True, "No session"),
    ]
    
    for session, require_mfa, description in session_tests:
        is_valid, message = check_session_validity(session, require_mfa)
        status = "✓" if is_valid else "✗"
        print(f"{status} {description:30} | {message}")


def demonstrate_password_strength() -> None:
    """
    Demonstrates password policy evaluation and feedback.
    
    Real-world use case: User registration, security audits.
    """
    test_passwords = [
        "weak",
        "Password1",
        "MyP@ssw0rd!",
        "SuperSecure123!@#",
    ]
    
    for pwd in test_passwords:
        strength, suggestions = determine_password_strength(pwd)
        
        strength_icons = {
            "weak": "🔴",
            "medium": "🟡",
            "strong": "🟢"
        }
        
        icon = strength_icons[strength]
        print(f"{icon} {strength.upper():6} | '{pwd}'")
        if suggestions:
            for suggestion in suggestions:
                print(f"           - {suggestion}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("USER AUTHENTICATION & SESSION MANAGEMENT".center(70))
    print("="*70)
    
    print("\n[1] USER AUTHENTICATION")
    print("-" * 70)
    demonstrate_authentication()
    
    print("\n\n[2] MFA VERIFICATION")
    print("-" * 70)
    demonstrate_mfa_verification()
    
    print("\n\n[3] SESSION VALIDATION")
    print("-" * 70)
    demonstrate_session_validation()
    
    print("\n\n[4] PASSWORD STRENGTH EVALUATION")
    print("-" * 70)
    demonstrate_password_strength()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Layer security checks: exists, expired, verified, authorized")
    print("2. Provide clear error messages without revealing security details")
    print("3. Implement account lockout to prevent brute force attacks")
    print("4. Use MFA for sensitive operations")
    print("5. Validate sessions before allowing protected actions")
    print("="*70)


if __name__ == "__main__":
    main()