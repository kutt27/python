"""
Python Functions: Encapsulation and Information Hiding
=======================================================

Topic: Hiding implementation details, public vs private interfaces

Real-World Applications:
- API design (public endpoints vs internal helpers)
- Library/SDK development
- Database abstraction layers
- Service interfaces
- Plugin systems
"""

from typing import Dict, List, Optional


def _validate_password_strength(password: str) -> bool:
    """
    Private helper: Validates password meets security requirements.
    
    Convention: Leading underscore indicates "internal use only".
    Users of the module should NOT call this directly.
    
    Args:
        password: Password to validate
    
    Returns:
        True if meets requirements
    
    Implementation detail hidden from public API.
    """
    has_length = len(password) >= 8
    has_number = any(c.isdigit() for c in password)
    has_letter = any(c.isalpha() for c in password)
    
    return has_length and has_number and has_letter


def _hash_password(password: str) -> str:
    """
    Private helper: Hashes password for storage.
    
    Implementation detail - users don't need to know HOW we hash.
    
    Args:
        password: Plain text password
    
    Returns:
        Hashed password
    
    In real app: use bcrypt/argon2, not this simplified version.
    """
    # Simplified - real apps use bcrypt/argon2
    return f"hashed_{password}_secure"


def _send_welcome_email(email: str) -> bool:
    """
    Private helper: Sends welcome email.
    
    Args:
        email: User's email address
    
    Returns:
        True if sent successfully
    
    Implementation detail hidden from public API.
    """
    print(f"    → Sending welcome email to {email}")
    return True


def register_user(username: str, email: str, password: str) -> Dict[str, any]:
    """
    PUBLIC API: Registers a new user.
    
    This is the public interface - clients call this function.
    Internal implementation details (_validate, _hash, _send_email)
    are hidden and can change without affecting clients.
    
    Args:
        username: Desired username
        email: User's email
        password: Plain text password
    
    Returns:
        Registration result dictionary
    
    Real-world use case: User registration API endpoint.
    """
    print(f"\nRegistering user: {username}")
    
    # Validation (using private helper)
    if not _validate_password_strength(password):
        return {
            "success": False,
            "error": "Password does not meet security requirements",
            "user_id": None
        }
    
    # Hash password (using private helper)
    hashed_pw = _hash_password(password)
    
    # Save to database (simulated)
    user_id = 12345
    print(f"  ✓ User created with ID: {user_id}")
    
    # Send welcome email (using private helper)
    _send_welcome_email(email)
    
    return {
        "success": True,
        "error": None,
        "user_id": user_id
    }


def _fetch_from_cache(key: str) -> Optional[Dict]:
    """
    Private helper: Attempts to fetch data from cache.
    
    Implementation detail - clients don't need to know about caching.
    """
    # Simulate cache lookup
    print(f"    → Checking cache for key: {key}")
    return None  # Cache miss


def _fetch_from_database(user_id: int) -> Dict:
    """
    Private helper: Fetches data from database.
    
    Implementation detail - clients don't care if data comes from
    cache or database.
    """
    print(f"    → Fetching user {user_id} from database")
    return {
        "id": user_id,
        "name": "Alice",
        "email": "alice@example.com"
    }


def _store_in_cache(key: str, data: Dict) -> None:
    """
    Private helper: Stores data in cache.
    
    Implementation detail for performance optimization.
    """
    print(f"    → Storing in cache: {key}")


def get_user(user_id: int) -> Optional[Dict]:
    """
    PUBLIC API: Retrieves user data.
    
    Encapsulation: Hides caching implementation from callers.
    They don't know or care if data comes from cache or database.
    
    Args:
        user_id: User identifier
    
    Returns:
        User data dictionary or None if not found
    
    Real-world use case: Data access layer with caching.
    """
    print(f"\nFetching user {user_id}")
    
    cache_key = f"user:{user_id}"
    
    # Try cache first (hidden from caller)
    cached_data = _fetch_from_cache(cache_key)
    if cached_data:
        print(f"  ✓ Cache hit!")
        return cached_data
    
    # Fetch from database (hidden from caller)
    data = _fetch_from_database(user_id)
    
    # Store in cache for next time (hidden from caller)
    _store_in_cache(cache_key, data)
    
    print(f"  ✓ User retrieved and cached")
    return data


class PaymentProcessor:
    """
    Example of encapsulation in a class.
    
    Public methods: process_payment()
    Private methods: _validate_card(), _charge_card(), _send_receipt()
    """
    
    def _validate_card(self, card_number: str) -> bool:
        """Private: Card validation logic."""
        print(f"    → Validating card ending in {card_number[-4:]}")
        return len(card_number) == 16
    
    def _charge_card(self, amount: float) -> str:
        """Private: Actual payment processing."""
        print(f"    → Charging ${amount:.2f}")
        return "TXN-12345"
    
    def _send_receipt(self, email: str, transaction_id: str) -> None:
        """Private: Receipt email."""
        print(f"    → Sending receipt to {email} (Transaction: {transaction_id})")
    
    def process_payment(self, card_number: str, amount: float, customer_email: str) -> Dict:
        """
        PUBLIC API: Processes payment.
        
        Clients only call this - implementation details hidden.
        
        Args:
            card_number: Credit card number
            amount: Payment amount
            customer_email: Customer email for receipt
        
        Returns:
            Payment result dictionary
        """
        print(f"\nProcessing payment of ${amount:.2f}")
        
        # Use private methods - implementation hidden
        if not self._validate_card(card_number):
            return {"success": False, "error": "Invalid card"}
        
        transaction_id = self._charge_card(amount)
        self._send_receipt(customer_email, transaction_id)
        
        return {
            "success": True,
            "transaction_id": transaction_id,
            "error": None
        }


def main() -> None:
    """Main function demonstrating encapsulation."""
    print("="*70)
    print("ENCAPSULATION & INFORMATION HIDING".center(70))
    print("="*70)
    
    print("\n[1] USER REGISTRATION - Public API, Hidden Implementation")
    print("="*70)
    
    # Good password
    result1 = register_user("alice", "alice@example.com", "SecurePass123")
    print(f"\nResult: {result1}")
    
    # Weak password
    result2 = register_user("bob", "bob@example.com", "weak")
    print(f"\nResult: {result2}")
    
    print("\n\n[2] DATA RETRIEVAL - Hidden Caching Layer")
    print("="*70)
    
    # First call - cache miss, hits database
    user1 = get_user(101)
    
    # Second call - cache hit (would be, if cache was real)
    user2 = get_user(101)
    
    print("\n\n[3] PAYMENT PROCESSING - Encapsulated Logic")
    print("="*70)
    
    processor = PaymentProcessor()
    payment_result = processor.process_payment(
        card_number="1234567812345678",
        amount=99.99,
        customer_email="customer@example.com"
    )
    print(f"\nPayment result: {payment_result}")
    
    print("\n\n" + "="*70)
    print("Benefits of Encapsulation:")
    print("-" * 70)
    print("✓ Simplicity: Public API is clean and simple to use")
    print("✓ Flexibility: Change implementation without affecting clients")
    print("✓ Security: Hide sensitive logic (hashing, validation)")
    print("✓ Maintainability: Internal changes don't break external code")
    print("✓ Testing: Test public interface, refactor internals freely")
    print("\nConvention: _leading_underscore indicates private/internal")
    print("="*70)


if __name__ == "__main__":
    main()