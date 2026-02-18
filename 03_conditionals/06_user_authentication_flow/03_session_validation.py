"""
Session Validation logic.
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


if __name__ == "__main__":
    demonstrate_session_validation()
