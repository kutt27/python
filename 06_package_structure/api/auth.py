"""
API Client Package - Authentication Module
===========================================

This module provides authentication functionality for the API client.

Real-World Application: OAuth2, API key management, token refresh
"""

from typing import Dict, Optional
from datetime import datetime, timedelta


class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass


class APIAuthenticator:
    """
    Handles API authentication and token management.
    
    Real-world use case: OAuth2 client, API key rotation.
    """
    
    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize authenticator.
        
        Args:
            api_key: API key
            api_secret: API secret
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self._access_token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None
    
    def authenticate(self) -> str:
        """
        Authenticates and returns access token.
        
        Returns:
            Access token
        
        Raises:
            AuthenticationError: If authentication fails
        """
        # Simulate API authentication
        if not self.api_key or not self.api_secret:
            raise AuthenticationError("Invalid credentials")
        
        # Generate token (simulated)
        self._access_token = f"token_{hash(self.api_key + self.api_secret)}"
        self._token_expires_at = datetime.now() + timedelta(hours=1)
        
        return self._access_token
    
    def get_token(self) -> str:
        """
        Gets current access token, refreshing if needed.
        
        Returns:
            Valid access token
        """
        if self._access_token is None or self._is_token_expired():
            return self.authenticate()
        
        return self._access_token
    
    def _is_token_expired(self) -> bool:
        """Checks if token is expired."""
        if self._token_expires_at is None:
            return True
        
        return datetime.now() >= self._token_expires_at


def create_auth_headers(token: str) -> Dict[str, str]:
    """
    Creates authentication headers for API requests.
    
    Args:
        token: Access token
    
    Returns:
        Headers dictionary
    
    Real-world use case: HTTP request headers.
    """
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
