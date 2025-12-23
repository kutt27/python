"""
Python Functions: Code Reusability and DRY Principle
=====================================================

Topic: Function basics, avoiding code duplication, DRY principle

Real-World Applications:
- API endpoint handlers
- Database query wrappers
- Logging utilities
- Data validation functions
- Business logic encapsulation
"""

from typing import Dict, List, Optional
from datetime import datetime


def log_api_request(method: str, endpoint: str, status_code: int) -> None:
    """
    Logs API request information.
    
    DRY Principle: Instead of duplicating logging code throughout
    the application, centralize it in a reusable function.
    
    Args:
        method: HTTP method
        endpoint: API endpoint path
        status_code: Response status code
    
    Real-world use case: API request logging, monitoring.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {method} {endpoint} - {status_code}")


def validate_email(email: str) -> bool:
    """
    Validates email format.
    
    DRY Principle: Email validation logic used in multiple places
    (registration, profile update, contact forms) - centralize it.
    
    Args:
        email: Email address to validate
    
    Returns:
        True if valid format, False otherwise
    
    Real-world use case: Form validation, user input checking.
    """
    # Simplified validation
    return "@" in email and "." in email.split("@")[1]


def calculate_discount(amount: float, discount_percent: float) -> float:
    """
    Calculates discounted amount.
    
    DRY Principle: Discount calculation used in cart, checkout,
    reports - avoid duplicating this business logic.
    
    Args:
        amount: Original amount
        discount_percent: Discount percentage (0-100)
    
    Returns:
        Discounted amount
    
    Real-world use case: E-commerce pricing, promotional calculations.
    """
    discount = amount * (discount_percent / 100)
    return amount - discount


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Formats amount as currency string.
    
    DRY Principle: Currency formatting needed in many views/reports.
    
    Args:
        amount: Numeric amount
        currency: Currency code
    
    Returns:
        Formatted currency string
    
    Real-world use case: Display formatting, financial reports.
    """
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "INR": "₹"}
    symbol = symbols.get(currency, "$")
    return f"{symbol}{amount:,.2f}"


def send_notification(user_id: int, message: str, channel: str = "email") -> bool:
    """
    Sends notification to user.
    
    DRY Principle: Notification sending logic centralized instead
    of duplicated across registration, password reset, order confirmation, etc.
    
    Args:
        user_id: User identifier
        message: Notification message
        channel: Notification channel (email/sms/push)
    
    Returns:
        True if sent successfully
    
    Real-world use case: User notifications, alert systems.
    """
    print(f"[{channel.upper()}] Sending to user {user_id}: {message}")
    # In real app: actual email/SMS sending logic
    return True



def demonstrate_api_logging() -> None:
    """
    Demonstrates reusable API request logging.
    
    Real-world use case: Observability in web applications.
    """
    # Same logging function used for all endpoints
    log_api_request("GET", "/api/users", 200)
    log_api_request("POST", "/api/orders", 201)
    log_api_request("DELETE", "/api/cache", 204)
    log_api_request("GET", "/api/products", 404)


def demonstrate_email_validation() -> None:
    """
    Demonstrates reusable email validation logic.
    
    Real-world use case: User registration and profile forms.
    """
    test_emails = [
        "user@example.com",
        "invalid.email",
        "admin@company.org",
        "@missing.com"
    ]
    
    for email in test_emails:
        is_valid = validate_email(email)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"  {status}: {email}")


def demonstrate_discount_calculation() -> None:
    """
    Demonstrates centralized business logic for discounts.
    
    Real-world use case: Pricing engines, e-commerce checkout.
    """
    orders = [
        ("Order #1", 100.00, 10),
        ("Order #2", 250.00, 20),
        ("Order #3", 75.00, 15),
    ]
    
    for order_id, amount, discount_pct in orders:
        final_amount = calculate_discount(amount, discount_pct)
        print(f"  {order_id}: {format_currency(amount)} - {discount_pct}% = {format_currency(final_amount)}")


def demonstrate_currency_formatting() -> None:
    """
    Demonstrates reusable display formatting for currencies.
    
    Real-world use case: International financial applications.
    """
    amounts = [1234.56, 9999.99, 42.00]
    currencies = ["USD", "EUR", "GBP", "INR"]
    
    for currency in currencies:
        formatted = [format_currency(amt, currency) for amt in amounts]
        print(f"  {currency}: {', '.join(formatted)}")


def demonstrate_notifications() -> None:
    """
    Demonstrates centralized communication logic.
    
    Real-world use case: Multi-channel alerting systems.
    """
    send_notification(101, "Welcome! Your account has been created.", "email")
    send_notification(101, "Your order #12345 has shipped.", "email")
    send_notification(102, "Password reset requested.", "sms")
    send_notification(103, "New message from support.", "push")


def main() -> None:
    """Main function demonstrating DRY principle with reusable functions."""
    print("="*70)
    print("PYTHON FUNCTIONS: DRY PRINCIPLE".center(70))
    print("="*70)
    
    print("\n[1] API REQUEST LOGGING - Reusable Across Endpoints")
    print("-" * 70)
    demonstrate_api_logging()
    
    print("\n\n[2] EMAIL VALIDATION - Reusable Across Forms")
    print("-" * 70)
    demonstrate_email_validation()
    
    print("\n\n[3] DISCOUNT CALCULATION - Reusable Business Logic")
    print("-" * 70)
    demonstrate_discount_calculation()
    
    print("\n\n[4] CURRENCY FORMATTING - Reusable Display Logic")
    print("-" * 70)
    demonstrate_currency_formatting()
    
    print("\n\n[5] NOTIFICATIONS - Reusable Communication Logic")
    print("-" * 70)
    demonstrate_notifications()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. DRY: Don't Repeat Yourself - write code once, use many times")
    print("2. Functions encapsulate reusable logic and reduce code bloat")
    print("3. Centralizing logic makes maintenance and debugging much easier")
    print("4. Descriptive function names document intent better than raw code")
    print("5. Functions provide a single point of truth for business rules")
    print("="*70)


if __name__ == "__main__":
    main()
