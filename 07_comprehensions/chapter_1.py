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



def demonstrate_data_filtering() -> None:
    """
    Demonstrates basic list comprehension for data filtering.
    
    Real-world use case: Isolating subsets of data based on flags.
    """
    users = [
        {"id": 1, "name": "Alice", "is_active": True},
        {"id": 2, "name": "Bob", "is_active": False},
        {"id": 3, "name": "Charlie", "is_active": True},
        {"id": 4, "name": "Diana", "is_active": False},
    ]
    
    # List comprehension (more Pythonic)
    active_users = [user["name"] for user in users if user["is_active"]]
    print(f"Active users: {active_users}")


def demonstrate_api_transformation() -> None:
    """
    Demonstrates data transformation during comprehension.
    
    Real-world use case: Reformatting API responses.
    """
    api_response = [
        {"user_id": 101, "full_name": "Alice Smith", "email_address": "alice@example.com"},
        {"user_id": 102, "full_name": "Bob Jones", "email_address": "bob@example.com"},
    ]
    
    user_emails = [user["email_address"].lower() for user in api_response]
    usernames = [user["full_name"].split()[0] for user in api_response]
    
    print(f"Emails: {user_emails}")
    print(f"First names: {usernames}")


def demonstrate_complex_filtering() -> None:
    """
    Demonstrates filtering with multiple criteria.
    
    Real-world use case: Complex business rule evaluation.
    """
    orders = [
        {"id": "ORD-001", "amount": 150, "status": "completed"},
        {"id": "ORD-002", "amount": 50, "status": "pending"},
        {"id": "ORD-003", "amount": 200, "status": "completed"},
        {"id": "ORD-004", "amount": 75, "status": "cancelled"},
    ]
    
    large_completed = [
        order["id"]
        for order in orders
        if order["status"] == "completed" and order["amount"] > 100
    ]
    print(f"Large completed orders: {large_completed}")


def demonstrate_nested_log_parsing() -> None:
    """
    Demonstrates nested comprehensions for hierarchical data.
    
    Real-world use case: Aggregating logs from multiple sources.
    """
    log_sources = [
        ["INFO: Server started", "ERROR: Connection timeout", "INFO: Request processed"],
        ["ERROR: Database error", "INFO: Cache hit"],
        ["ERROR: Invalid input", "INFO: Response sent"],
    ]
    
    all_errors = [
        log_line
        for source in log_sources
        for log_line in source
        if "ERROR" in log_line
    ]
    
    print("All error logs:")
    for error in all_errors:
        print(f"  - {error}")


def demonstrate_email_validation() -> None:
    """
    Demonstrates basic string processing in comprehensions.
    
    Real-world use case: Rapid input validation.
    """
    email_list = [
        "alice@example.com",
        "invalid.email",
        "bob@company.org",
        "@missing.com",
        "charlie@test.io",
    ]
    
    valid_emails = [
        email
        for email in email_list
        if "@" in email and "." in email.split("@")[-1]
    ]
    print(f"Valid emails: {valid_emails}")


def demonstrate_math_transformations() -> None:
    """
    Demonstrates algebraic transformations in-place.
    
    Real-world use case: Price adjustments, unit conversions.
    """
    prices = [100, 250, 75, 150, 300]
    discount_percent = 20
    
    discounted_prices = [price * (1 - discount_percent / 100) for price in prices]
    print(f"Original: {prices}")
    print(f"Discounted (20%): {[f'${p:.2f}' for p in discounted_prices]}")


def demonstrate_conditional_expressions() -> None:
    """
    Demonstrates ternary logic within comprehensions.
    
    Real-world use case: Categorizing metrics or data points.
    """
    order_amounts = [25, 150, 75, 300, 50]
    order_categories = ["Large" if amount > 100 else "Small" for amount in order_amounts]
    
    print("Order categorization:")
    for amount, category in zip(order_amounts, order_categories):
        print(f"  ${amount}: {category}")


def demonstrate_feature_extraction() -> None:
    """
    Demonstrates extraction from text corpora.
    
    Real-world use case: NLP preprocessing, search indexing.
    """
    text_samples = [
        "Machine learning is amazing",
        "Python programming tutorial",
        "Learn data science today",
    ]
    long_words = [
        word
        for text in text_samples
        for word in text.split()
        if len(word) > 5
    ]
    print(f"Words > 5 chars: {long_words}")


def demonstrate_list_flattening() -> None:
    """
    Demonstrates how to flatten nested list structures.
    
    Real-world use case: Normalizing deeply nested data.
    """
    nested_data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flattened = [item for sublist in nested_data for item in sublist]
    
    print(f"Nested: {nested_data}")
    print(f"Flattened: {flattened}")


def demonstrate_db_processing() -> None:
    """
    Demonstrates processing query results using unpacking.
    
    Real-world use case: Analyzing relational data.
    """
    db_results = [
        (1, "Alice", "Engineering", 95000),
        (2, "Bob", "Marketing", 75000),
        (3, "Charlie", "Engineering", 105000),
        (4, "Diana", "Sales", 85000),
    ]
    
    engineering_salaries = [
        salary
        for (id, name, dept, salary) in db_results
        if dept == "Engineering"
    ]
    
    print(f"Engineering salaries: {engineering_salaries}")
    if engineering_salaries:
        print(f"Average: ${sum(engineering_salaries) / len(engineering_salaries):,.2f}")


def main() -> None:
    """Main function to run all demonstrations for list comprehensions."""
    print("="*70)
    print("PYTHON LIST COMPREHENSIONS".center(70))
    print("="*70)
    
    print("\n[1] DATA FILTERING")
    print("-" * 70)
    demonstrate_data_filtering()
    
    print("\n\n[2] API TRANSFORMATION")
    print("-" * 70)
    demonstrate_api_transformation()
    
    print("\n\n[3] COMPLEX FILTERING")
    print("-" * 70)
    demonstrate_complex_filtering()
    
    print("\n\n[4] LOG PARSING (NESTED)")
    print("-" * 70)
    demonstrate_nested_log_parsing()
    
    print("\n\n[5] STRING PROCESSING")
    print("-" * 70)
    demonstrate_email_validation()
    
    print("\n\n[6] MATH TRANSFORMATIONS")
    print("-" * 70)
    demonstrate_math_transformations()
    
    print("\n\n[7] CONDITIONAL EXPRESSIONS")
    print("-" * 70)
    demonstrate_conditional_expressions()
    
    print("\n\n[8] FEATURE EXTRACTION")
    print("-" * 70)
    demonstrate_feature_extraction()
    
    print("\n\n[9] LIST FLATTENING")
    print("-" * 70)
    demonstrate_list_flattening()
    
    print("\n\n[10] DATABASE RESULT PROCESSING")
    print("-" * 70)
    demonstrate_db_processing()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. [expr for item in iterable if cond] is the standard syntax")
    print("2. List comprehensions are more concise and often faster than loops")
    print("3. Nesting multiple 'for' clauses allows flattening sublists")
    print("4. Use if/else before 'for' for conditional values (ternary)")
    print("5. Use if after 'for' for filtering elements from the sequence")
    print("="*70)


if __name__ == "__main__":
    main()