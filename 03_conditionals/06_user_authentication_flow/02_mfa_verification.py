"""
MFA Verification logic.
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


if __name__ == "__main__":
    demonstrate_mfa_verification()
