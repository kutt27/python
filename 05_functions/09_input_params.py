"""
Python Function Parameters: Advanced Patterns
==============================================

Topic: Positional, keyword, args, kwargs, default parameters

Real-World Applications:
- Flexible API design
- Decorator implementation
- Wrapper functions
- Configuration builders
- Variadic functions
"""

from typing import Dict, List, Any, Tuple


def create_user(username: str, email: str, *, is_active: bool = True, role: str = "user") -> Dict:
    """
    Creates user with keyword-only parameters.
    
    The * forces is_active and role to be keyword-only.
    
    Args:
        username: User's username (positional)
        email: User's email (positional)
        is_active: Account status (keyword-only)
        role: User role (keyword-only)
    
    Returns:
        User dictionary
    
    Real-world use case: User management with clear API.
    """
    return {
        "username": username,
        "email": email,
        "is_active": is_active,
        "role": role
    }


def log_message(message: str, /, level: str = "INFO", **metadata) -> None:
    """
    Logs message with flexible metadata.
    
    The / makes message positional-only (Python 3.8+).
    **metadata accepts any keyword arguments.
    
    Args:
        message: Log message (positional-only)
        level: Log level
        **metadata: Additional metadata
    
    Real-world use case: Structured logging.
    """
    meta_str = ", ".join(f"{k}={v}" for k, v in metadata.items())
    print(f"[{level}] {message}" + (f" | {meta_str}" if meta_str else ""))


def make_api_request(*endpoints, method: str = "GET", **params) -> List[Dict]:
    """
    Makes API requests to multiple endpoints.
    
    *endpoints accepts any number of positional arguments.
    **params accepts request parameters as keywords.
    
    Args:
        *endpoints: API endpoints to query
        method: HTTP method
        **params: Query parameters
    
    Returns:
        List of responses
    
    Real-world use case: Batch API requests.
    """
    responses = []
    
    print(f"\nMaking {method} requests:")
    for endpoint in endpoints:
        param_str = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{endpoint}?{param_str}" if params else endpoint
        
        print(f"  {method} {url}")
        responses.append({"endpoint": endpoint, "status": 200, "method": method})
    
    return responses


def configure_database(
    host: str = "localhost",
    port: int = 5432,
    database: str = "app_db",
    **options
) -> Dict[str, Any]:
    """
    Configures database connection with flexible options.
    
    Args:
        host: Database host
        port: Database port
        database: Database name
        **options: Additional connection options
    
    Returns:
        Configuration dictionary
    
    Real-world use case: Database configuration builder.
    """
    config = {
        "host": host,
        "port": port,
        "database": database,
        **options  # Merge additional options
    }
    
    return config


def process_payment(
    amount: float,
    /,  # positional-only
    *,  # keyword-only after this
    card_number: str,
    cvv: str,
    billing_zip: str = None
) -> Dict:
    """
    Processes payment with strict parameter types.
    
    Args:
        amount: Payment amount (positional-only)
        card_number: Card number (keyword-only)
        cvv: CVV code (keyword-only)
        billing_zip: Billing ZIP code (keyword-only, optional)
    
    Returns:
        Transaction result
    
    Real-world use case: Payment processing with clear API.
    """
    return {
        "amount": amount,
        "card_last_four": card_number[-4:],
        "billing_zip": billing_zip,
        "status": "approved"
    }


def build_query(*select_fields, table: str, **where_conditions) -> str:
    """
    Builds SQL query dynamically.
    
    Args:
        *select_fields: Fields to select
        table: Table name
        **where_conditions: WHERE clause conditions
    
    Returns:
        SQL query string
    
    Real-world use case: Query builder, ORM implementation.
    """
    # SELECT clause
    fields = ", ".join(select_fields) if select_fields else "*"
    
    # WHERE clause
    where = ""
    if where_conditions:
        conditions = [f"{k} = '{v}'" for k, v in where_conditions.items()]
        where = " WHERE " + " AND ".join(conditions)
    
    query = f"SELECT {fields} FROM {table}{where}"
    return query


def create_api_wrapper(*args, **kwargs):
    """
    Example wrapper accepting any arguments.
    
    Common pattern for decorators and proxy functions.
    
    Args:
        *args: Positional arguments to forward
        **kwargs: Keyword arguments to forward
    
    Real-world use case: Decorators, middleware, proxies.
    """
    print(f"  Wrapper called with:")
    print(f"    args: {args}")
    print(f"    kwargs: {kwargs}")
    
    # Forward to actual function
    return {"forwarded_args": args, "forwarded_kwargs": kwargs}


def main() -> None:
    """Main function demonstrating parameter patterns."""
    print("="*70)
    print("FUNCTION PARAMETERS: ADVANCED PATTERNS".center(70))
    print("="*70)
    
    print("\n[1] KEYWORD-ONLY PARAMETERS (*)")
    print("=" * 70)
    
    user1 = create_user("alice", "alice@example.com", role="admin")
    user2 = create_user("bob", "bob@example.com", is_active=False)
    
    print(f"User 1: {user1}")
    print(f"User 2: {user2}")
    
    # This would error: create_user("alice", "alice@example.com", True, "admin")
    # Must use keywords: create_user("alice", "alice@example.com", is_active=True, role="admin")
    
    print("\n\n[2] POSITIONAL-ONLY PARAMETERS (/)")
    print("=" * 70)
    
    log_message("Application started")
    log_message("Request processed", level="DEBUG", user_id=101, duration_ms=45)
    log_message("Error occurred", level="ERROR", error_code="E001", trace_id="abc123")
    
    print("\n\n[3] VARIADIC FUNCTIONS (*args, **kwargs)")
    print("=" * 70)
    
    make_api_request(
        "/api/users",
        "/api/products",
        "/api/orders", method="GET",
        limit=10,
        offset=0,
        include_deleted=False
    )
    
    print("\n\n[4] CONFIGURATION BUILDER")
    print("=" * 70)
    
    db_config = configure_database(
        host="prod-db.example.com",
        port=5432,
        database="production",
        pool_size=20,
        ssl_mode="require",
        connect_timeout=30
    )
    
    print("Database configuration:")
    for key, value in db_config.items():
        print(f"  {key}: {value}")
    
    print("\n\n[5] STRICT PARAMETER API")
    print("=" * 70)
    
    # Must use keywords for sensitive data
    payment = process_payment(
        99.99,  # positional amount
        card_number="1234567812345678",
        cvv="123",
        billing_zip="12345"
    )
    
    print(f"Payment processed: {payment}")
    
    print("\n\n[6] SQL QUERY BUILDER")
    print("=" * 70)
    
    queries = [
        build_query("id", "name", "email", table="users"),
        build_query("*", table="products", category="electronics", in_stock=True),
        build_query(table="orders", user_id=101, status="completed"),
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"Query {i}: {query}")
    
    print("\n\n[7] GENERIC WRAPPER")
    print("=" * 70)
    
    result = create_api_wrapper(
        "arg1", "arg2", 123,
        keyword1="value1",
        keyword2="value2",
        config={"debug": True}
    )
    
    print("\n" + "="*70)
    print("Parameter Types Summary:")
    print("-" * 70)
    print("def func(pos_only, /, pos_or_kw, *, kw_only, **kwargs):")
    print("  • pos_only: Positional-only (before /)")
    print("  • pos_or_kw: Positional or keyword")
    print("  • kw_only: Keyword-only (after *)")
    print("  • *args: Variable positional arguments")
    print("  • **kwargs: Variable keyword arguments")
    print("\nBest Practices:")
    print("  ✓ Use keyword-only for boolean/optional parameters")
    print("  ✓ Use positional-only for required, obvious parameters")
    print("  ✓ Use **kwargs for flexible, extensible APIs")
    print("  ✓ Always provide defaults for optional parameters")
    print("="*70)


if __name__ == "__main__":
    main()