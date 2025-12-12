"""
Python Exceptions: Advanced Custom Exceptions
==============================================

Topic: Custom exceptions with attributes and payloads

Real-World Applications:
- API Error responses with status codes and internal codes
- Validation errors with field names
- Complex error reporting systems
"""

from typing import Any, Dict, Optional
import datetime

class APIError(Exception):
    """
    Base API Exception with status code and error details.
    """
    def __init__(self, message: str, status_code: int = 500, details: Optional[Dict] = None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details or {}
        self.timestamp = datetime.datetime.now()
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for JSON response."""
        return {
            "error": str(self),
            "status": self.status_code,
            "details": self.details,
            "timestamp": self.timestamp.isoformat()
        }


class RateLimitExceeded(APIError):
    """Raised when API rate limit is breached."""
    def __init__(self, limit: int, reset_in: int):
        super().__init__(
            message="Rate limit exceeded", 
            status_code=429,
            details={"limit": limit, "retry_after_seconds": reset_in}
        )


class PaymentDeclined(APIError):
    """Raised when payment fails."""
    def __init__(self, transaction_id: str, code: str):
        super().__init__(
            message="Payment transaction declined",
            status_code=402,
            details={"transaction_id": transaction_id, "decline_code": code}
        )


def process_api_request(request_type: str):
    """
    Simulate API request processing.
    """
    print(f"\nProcessing request: {request_type}")
    
    if request_type == "spam":
        raise RateLimitExceeded(limit=100, reset_in=60)
        
    if request_type == "bad_card":
        raise PaymentDeclined(transaction_id="TXN_12345", code="INSUFFICIENT_FUNDS")
        
    print("✓ Request processed successfully")


def main():
    """Demonstrates advanced custom exceptions."""
    print("="*70)
    print("ADVANCED CUSTOM EXCEPTIONS".center(70))
    print("="*70)
    
    requests = ["spam", "bad_card", "normal"]
    
    for req in requests:
        try:
            process_api_request(req)
            
        except APIError as e:
            # Handle all API errors uniformly
            print(f"✗ Caught API Error: {type(e).__name__}")
            print(f"  Status Code: {e.status_code}")
            print(f"  JSON Response: {e.to_dict()}")
            
    print("\n" + "="*70)
    print("Key Points:")
    print("• Custom exceptions can store additional state (codes, timestamps)")
    print("• Useful for converting exceptions to structured responses (JSON)")
    print("• Simplifies error handling middleware in web frameworks")
    print("="*70)


if __name__ == "__main__":
    main()