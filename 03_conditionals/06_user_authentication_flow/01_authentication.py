"""
Authentication logic.
"""

from typing import Optional
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


if __name__ == "__main__":
    demonstrate_authentication()
