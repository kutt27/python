"""
Python List Comprehensions
===========================

Topic: List comprehensions for concise list creation and filtering

Real-World Applications:
- Data filtering and transformation
- API response processing
- Log parsing
- Feature extraction
- Batch data cleaning
"""

from typing import List, Dict
import re


def main() -> None:
    """Main function demonstrating list comprehensions."""
    print("="*70)
    print("LIST COMPREHENSIONS".center(70))
    print("="*70)
    
    print("\n[1] BASIC LIST COMPREHENSION - Data Filtering")
    print("-" * 70)
    
    # Filter active users
    users = [
        {"id": 1, "name": "Alice", "is_active": True},
        {"id": 2, "name": "Bob", "is_active": False},
        {"id": 3, "name": "Charlie", "is_active": True},
        {"id": 4, "name": "Diana", "is_active": False},
    ]
    
    # Traditional approach
    active_users_loop = []
    for user in users:
        if user["is_active"]:
            active_users_loop.append(user["name"])
    
    # List comprehension (more Pythonic)
    active_users = [user["name"] for user in users if user["is_active"]]
    
    print(f"Active users: {active_users}")
    
    print("\n\n[2] TRANSFORMATION - API Response Processing")
    print("-" * 70)
    
    # Transform API response
    api_response = [
        {"user_id": 101, "full_name": "Alice Smith", "email_address": "alice@example.com"},
        {"user_id": 102, "full_name": "Bob Jones", "email_address": "bob@example.com"},
    ]
    
    # Extract and format
    user_emails = [
        user["email_address"].lower()
        for user in api_response
    ]
    
    usernames = [
        user["full_name"].split()[0]
        for user in api_response
    ]
    
    print(f"Emails: {user_emails}")
    print(f"First names: {usernames}")
    
    print("\n\n[3] FILTERING WITH COMPLEX CONDITIONS")
    print("-" * 70)
    
    # Filter orders
    orders = [
        {"id": "ORD-001", "amount": 150, "status": "completed"},
        {"id": "ORD-002", "amount": 50, "status": "pending"},
        {"id": "ORD-003", "amount": 200, "status": "completed"},
        {"id": "ORD-004", "amount": 75, "status": "cancelled"},
    ]
    
    # Completed orders over $100
    large_completed = [
        order["id"]
        for order in orders
        if order["status"] == "completed" and order["amount"] > 100
    ]
    
    print(f"Large completed orders: {large_completed}")
    
    print("\n\n[4] NESTED LIST COMPREHENSION - Log Parsing")
    print("-" * 70)
    
    # Parse error logs from multiple sources
    log_sources = [
        ["INFO: Server started", "ERROR: Connection timeout", "INFO: Request processed"],
        ["ERROR: Database error", "INFO: Cache hit"],
        ["ERROR: Invalid input", "INFO: Response sent"],
    ]
    
    # Extract all errors from all sources
    all_errors = [
        log_line
        for source in log_sources
        for log_line in source
        if "ERROR" in log_line
    ]
    
    print("All error logs:")
    for error in all_errors:
        print(f"  - {error}")
    
    print("\n\n[5] STRING PROCESSING - Email Validation")
    print("-" * 70)
    
    email_list = [
        "alice@example.com",
        "invalid.email",
        "bob@company.org",
        "@missing.com",
        "charlie@test.io",
    ]
    
    # Filter valid emails (basic check)
    valid_emails = [
        email
        for email in email_list
        if "@" in email and "." in email.split("@")[-1]
    ]
    
    print(f"Valid emails: {valid_emails}")
    
    print("\n\n[6] MATHEMATICAL TRANSFORMATIONS")
    print("-" * 70)
    
    # Calculate discounted prices
    prices = [100, 250, 75, 150, 300]
    discount_percent = 20
    
    discounted_prices = [
        price * (1 - discount_percent / 100)
        for price in prices
    ]
    
    print(f"Original: {prices}")
    print(f"Discounted (20%): {[f'${p:.2f}' for p in discounted_prices]}")
    
    print("\n\n[7] CONDITIONAL EXPRESSIONS IN COMPREHENSIONS")
    print("-" * 70)
    
    # Categorize order sizes
    order_amounts = [25, 150, 75, 300, 50]
    
    order_categories = [
        "Large" if amount > 100 else "Small"
        for amount in order_amounts
    ]
    
    print("Order categorization:")
    for amount, category in zip(order_amounts, order_categories):
        print(f"  ${amount}: {category}")
    
    print("\n\n[8] FEATURE EXTRACTION - ML/AI Use Case")
    print("-" * 70)
    
    # Extract features from text data
    text_samples = [
        "Machine learning is amazing",
        "Python programming tutorial",
        "Learn data science today",
    ]
    
    # Extract words longer than 5 characters
    long_words = [
        word
        for text in text_samples
        for word in text.split()
        if len(word) > 5
    ]
    
    print(f"Words > 5 chars: {long_words}")
    
    print("\n\n[9] FLATTENING NESTED LISTS")
    print("-" * 70)
    
    # Flatten nested list structure
    nested_data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    
    flattened = [
        item
        for sublist in nested_data
        for item in sublist
    ]
    
    print(f"Nested: {nested_data}")
    print(f"Flattened: {flattened}")
    
    print("\n\n[10] REAL-WORLD: DATABASE QUERY RESULT PROCESSING")
    print("-" * 70)
    
    # Simulate database query results
    db_results = [
        (1, "Alice", "Engineering", 95000),
        (2, "Bob", "Marketing", 75000),
        (3, "Charlie", "Engineering", 105000),
        (4, "Diana", "Sales", 85000),
    ]
    
    # Extract engineering department salaries
    engineering_salaries = [
        salary
        for (id, name, dept, salary) in db_results
        if dept == "Engineering"
    ]
    
    print(f"Engineering salaries: {engineering_salaries}")
    print(f"Average: ${sum(engineering_salaries) / len(engineering_salaries):,.2f}")
    
    print("\n" + "="*70)
    print("List Comprehension Syntax:")
    print("-" * 70)
    print("[expression for item in iterable if condition]")
    print("\nEquivalent to:")
    print("result = []")
    print("for item in iterable:")
    print("    if condition:")
    print("        result.append(expression)")
    print("\nBenefits:")
    print("✓ More concise and readable")
    print("✓ Often faster than equivalent loop")
    print("✓ Creates new list (doesn't modify original)")
    print("✓ Pythonic idiom for transformations/filtering")
    print("="*70)


if __name__ == "__main__":
    main()