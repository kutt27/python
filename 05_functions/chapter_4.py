"""
Python Functions: Parameters and Return Values
===============================================

Topic: Function parameters, return values, multiple returns

Real-World Applications:
- API request handlers with typed parameters
- Data transformation functions
- Calculation utilities
- Validation functions with results
- Business logic with computed values
"""

from typing import Tuple, Optional, Dict, List


def calculate_tax_and_total(subtotal: float, tax_rate: float = 0.08) -> Tuple[float, float]:
    """
    Calculates tax amount and total.
    
    Args:
        subtotal: Order subtotal
        tax_rate: Tax rate (default 8%)
    
    Returns:
        Tuple of (tax_amount, total_with_tax)
    
    Real-world use case: E-commerce checkout calculation.
    """
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return (tax_amount, total)


def process_payment(
    amount: float,
    card_number: str,
    cvv: str,
    charge_fee: bool = True
) -> Dict[str, any]:
    """
    Processes payment and returns detailed result.
    
    Args:
        amount: Payment amount
        card_number: Card number
        cvv: Card security code
        charge_fee: Whether to add processing fee (default True)
    
    Returns:
        Dictionary with transaction details
    
    Real-world use case: Payment processing system.
    """
    # Calculate processing fee
    processing_fee = amount * 0.029 if charge_fee else 0.0
    total_charged = amount + processing_fee
    
    # Simulate payment processing
    transaction_id = f"TXN-{hash(card_number + cvv) % 100000:05d}"
    
    return {
        "success": True,
        "transaction_id": transaction_id,
        "amount": amount,
        "fee": processing_fee,
        "total_charged": total_charged,
        "last_four": card_number[-4:]
    }


def validate_user_input(
    username: str,
    email: str,
    password: str,
    min_password_length: int = 8
) -> Tuple[bool, Optional[str]]:
    """
    Validates user registration input.
    
    Args:
        username: Desired username
        email: Email address
        password: Password
        min_password_length: Minimum password length
    
    Returns:
        Tuple of (is_valid, error_message)
        error_message is None if valid
    
    Real-world use case: Form validation, user registration.
    """
    # Username validation
    if len(username) < 3:
        return (False, "Username must be at least 3 characters")
    
    # Email validation
    if "@" not in email or "." not in email.split("@")[1]:
        return (False, "Invalid email format")
    
    # Password validation
    if len(password) < min_password_length:
        return (False, f"Password must be at least {min_password_length} characters")
    
    if not any(c.isdigit() for c in password):
        return (False, "Password must contain at least one number")
    
    return (True, None)


def calculate_shipping_cost(
    weight_kg: float,
    distance_km: float,
    express: bool = False,
    insurance: bool = False
) -> Dict[str, float]:
    """
    Calculates shipping cost with breakdown.
    
    Args:
        weight_kg: Package weight in kg
        distance_km: Shipping distance in km
        express: Express shipping option
        insurance: Insurance option
    
    Returns:
        Dictionary with cost breakdown
    
    Real-world use case: Logistics cost calculation.
    """
    # Base cost
    base_cost = 5.00
    
    # Weight cost
    weight_cost = weight_kg * 2.50
    
    # Distance cost
    distance_cost = distance_km * 0.15
    
    # Express surcharge
    express_cost = 15.00 if express else 0.0
    
    # Insurance cost
    insurance_cost = 3.00 if insurance else 0.0
    
    # Total
    total_cost = base_cost + weight_cost + distance_cost + express_cost + insurance_cost
    
    return {
        "base": base_cost,
        "weight": weight_cost,
        "distance": distance_cost,
        "express": express_cost,
        "insurance": insurance_cost,
        "total": total_cost
    }


def parse_api_response(response_text: str, expected_format: str = "json") -> Tuple[bool, any]:
    """
    Parses API response text into structured data.
    
    Args:
        response_text: Raw response text
        expected_format: Expected format (json/xml/text)
    
    Returns:
        Tuple of (success, parsed_data_or_error)
    
    Real-world use case: API client implementation.
    """
    try:
        if expected_format == "json":
            # Simulate JSON parsing
            if response_text.startswith("{"):
                return (True, {"status": "success", "data": response_text})
            else:
                return (False, "Invalid JSON format")
        elif expected_format == "xml":
            # Simulate XML parsing
            if response_text.startswith("<"):
                return (True, {"status": "success", "xml": response_text})
            else:
                return (False, "Invalid XML format")
        else:
            return (True, response_text)
    
    except Exception as e:
        return (False, str(e))


def main() -> None:
    """Main function demonstrating parameters and return values."""
    print("="*70)
    print("FUNCTION PARAMETERS & RETURN VALUES".center(70))
    print("="*70)
    
    print("\n[1] TAX CALCULATION - Multiple Return Values")
    print("-" * 70)
    
    orders = [100.00, 250.00, 75.50]
    
    for subtotal in orders:
        tax, total = calculate_tax_and_total(subtotal, tax_rate=0.08)
        print(f"  Subtotal: ${subtotal:.2f} | Tax: ${tax:.2f} | Total: ${total:.2f}")
    
    print("\n\n[2] PAYMENT PROCESSING - Dictionary Return")
    print("-" * 70)
    
    result = process_payment(
        amount=99.99,
        card_number="1234567812345678",
        cvv="123",
        charge_fee=True
    )
    
    print(f"  Transaction: {result['transaction_id']}")
    print(f"  Amount: ${result['amount']:.2f}")
    print(f"  Processing Fee: ${result['fee']:.2f}")
    print(f"  Total Charged: ${result['total_charged']:.2f}")
    print(f"  Card: ****{result['last_four']}")
    
    print("\n\n[3] INPUT VALIDATION - Boolean + Optional Error")
    print("-" * 70)
    
    test_inputs = [
        ("alice", "alice@example.com", "SecurePass123"),
        ("ab", "alice@example.com", "SecurePass123"),  # Short username
        ("alice", "invalid-email", "SecurePass123"),  # Bad email
        ("alice", "alice@example.com", "short"),  # Weak password
    ]
    
    for username, email, password in test_inputs:
        is_valid, error = validate_user_input(username, email, password)
        
        if is_valid:
            print(f"  ✓ Valid: {username}")
        else:
            print(f"  ✗ Invalid: {username} - {error}")
    
    print("\n\n[4] SHIPPING COST CALCULATION - Detailed Breakdown")
    print("-" * 70)
    
    shipping_scenarios = [
        (2.5, 50, False, False, "Standard domestic"),
        (5.0, 200, True, False, "Express long distance"),
        (1.0, 25, False, True, "Standard with insurance"),
    ]
    
    for weight, distance, express, insurance, description in shipping_scenarios:
        cost_breakdown = calculate_shipping_cost(weight, distance, express, insurance)
        
        print(f"\n  {description}:")
        print(f"    Weight: {weight}kg, Distance: {distance}km")
        print(f"    Base: ${cost_breakdown['base']:.2f}")
        print(f"    Weight: ${cost_breakdown['weight']:.2f}")
        print(f"    Distance: ${cost_breakdown['distance']:.2f}")
        if cost_breakdown['express'] > 0:
            print(f"    Express: ${cost_breakdown['express']:.2f}")
        if cost_breakdown['insurance'] > 0:
            print(f"    Insurance: ${cost_breakdown['insurance']:.2f}")
        print(f"    TOTAL: ${cost_breakdown['total']:.2f}")
    
    print("\n\n[5] API RESPONSE PARSING - Error Handling Returns")
    print("-" * 70)
    
    responses = [
        ('{"data": "value"}', "json"),
        ('<xml>data</xml>', "xml"),
        ('invalid json', "json"),
    ]
    
    for response_text, format_type in responses:
        success, result = parse_api_response(response_text, format_type)
        
        if success:
            print(f"  ✓ Parsed {format_type}: {result}")
        else:
            print(f"  ✗ Parse error: {result}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Use type hints for parameters and return values")
    print("2. Default parameters make functions flexible")
    print("3. Return tuples for multiple values")
    print("4. Return dictionaries for structured results")
    print("5. Return (success, result) pattern for operations that can fail")
    print("="*70)


if __name__ == "__main__":
    main()