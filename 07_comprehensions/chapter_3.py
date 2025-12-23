"""
Python Dictionary Comprehensions
==================================

Topic: Dictionary comprehensions for transforming and filtering dictionaries

Real-World Applications:
- Currency conversion
- Data normalization
- Configuration transformations
- API response reshaping
- Key-value pair filtering
"""

from typing import Dict


def main() -> None:
    """Main function demonstrating dictionary comprehensions."""
    print("="*70)
    print("DICTIONARY COMPREHENSIONS".center(70))
    print("="*70)
    
    print("\n[1] BASIC TRANSFORMATION - Currency Conversion")
    print("-" * 70)
    
    prices_usd = {
        "laptop": 999,
        "mouse": 29,
        "keyboard": 79,
        "monitor": 299
    }
    
    # Convert USD to EUR (rate: 0.92)
    prices_eur = {
        product: price * 0.92
        for product, price in prices_usd.items()
    }
    
    print("Prices in USD:")
    for product, price in prices_usd.items():
        print(f"  {product}: ${price}")
    
    print("\nPrices in EUR:")
    for product, price in prices_eur.items():
        print(f"  {product}: €{price:.2f}")
    
    print("\n\n[2] FILTERING - Active Users")
    print("-" * 70)
    
    users = {
        101: {"name": "Alice", "is_active": True},
        102: {"name": "Bob", "is_active": False},
        103: {"name": "Charlie", "is_active": True},
        104: {"name": "Diana", "is_active": False},
    }
    
    # Keep only active users
    active_users = {
        user_id: user_data
        for user_id, user_data in users.items()
        if user_data["is_active"]
    }
    
    print(f"Active users: {active_users}")
    
    print("\n\n[3] KEY-VALUE SWAP - Reverse Mapping")
    print("-" * 70)
    
    error_codes = {
        404: "Not Found",
        500: "Internal Server Error",
        403: "Forbidden",
        200: "OK"
    }
    
    # Reverse: message -> code
    message_to_code = {
        message: code
        for code, message in error_codes.items()
    }
    
    print("Code to message:")
    for code, msg in error_codes.items():
        print(f"  {code}: {msg}")
    
    print("\nMessage to code:")
    for msg, code in message_to_code.items():
        print(f"  '{msg}': {code}")
    
    print("\n\n[4] NESTED DATA TRANSFORMATION")
    print("-" * 70)
    
    # Transform user data
    raw_users = [
        {"id": 1, "username": "alice", "email": "ALICE@EXAMPLE.COM"},
        {"id": 2, "username": "bob", "email": "BOB@COMPANY.ORG"},
    ]
    
    # Create dict with normalized emails
    users_by_id = {
        user["id"]: {
            "username": user["username"],
            "email": user["email"].lower()
        }
        for user in raw_users
    }
    
    print("Normalized users:")
    for user_id, data in users_by_id.items():
        print(f"  User {user_id}: {data}")
    
    print("\n\n[5] CALCULATED VALUES - Inventory Value")
    print("-" * 70)
    
    inventory = {
        "laptop": {"quantity": 10, "unit_price": 999},
        "mouse": {"quantity": 50, "unit_price": 29},
        "keyboard": {"quantity": 30, "unit_price": 79},
    }
    
    # Calculate total value per item
    inventory_values = {
        item: data["quantity"] * data["unit_price"]
        for item, data in inventory.items()
    }
    
    print("Inventory values:")
    for item, value in inventory_values.items():
        print(f"  {item}: ${value:,}")
    
    total_value = sum(inventory_values.values())
    print(f"\nTotal inventory value: ${total_value:,}")
    
    print("\n\n[6] CONDITIONAL TRANSFORMATION - Discount Application")
    print("-" * 70)
    
    orders = {
        "ORD-001": 150,
        "ORD-002": 50,
        "ORD-003": 200,
        "ORD-004": 75,
    }
    
    # Apply 10% discount to orders > $100
    discounted_orders = {
        order_id: amount * 0.9 if amount > 100 else amount
        for order_id, amount in orders.items()
    }
    
    print("Order totals (discount applied for > $100):")
    for order_id, amount in discounted_orders.items():
        original = orders[order_id]
        discount_applied = original != amount
        status = f"(${original} - 10%)" if discount_applied else ""
        print(f"  {order_id}: ${amount:.2f} {status}")
    
    print("\n\n[7] GROUPING DATA - Average by Category")
    print("-" * 70)
    
    products = [
        {"name": "Laptop", "category": "electronics", "price": 999},
        {"name": "Mouse", "category": "electronics", "price": 29},
        {"name": "Desk", "category": "furniture", "price": 299},
        {"name": "Chair", "category": "furniture", "price": 199},
    ]
    
    # Group prices by category (for averaging)
    category_prices = {}
    for product in products:
        cat = product["category"]
        if cat not in category_prices:
            category_prices[cat] = []
        category_prices[cat].append(product["price"])
    
    # Calculate averages
    category_averages = {
        category: sum(prices) / len(prices)
        for category, prices in category_prices.items()
    }
    
    print("Average prices by category:")
    for category, avg_price in category_averages.items():
        print(f"  {category}: ${avg_price:.2f}")
    
    print("\n\n[8] API RESPONSE RESHAPING")
    print("-" * 70)
    
    # API returns list, we want dict keyed by ID
    api_response = [
        {"user_id": 101, "name": "Alice", "role": "admin"},
        {"user_id": 102, "name": "Bob", "role": "user"},
        {"user_id": 103, "name": "Charlie", "role": "moderator"},
    ]
    
    # Reshape to dict for O(1) lookups
    users_dict = {
        user["user_id"]: {"name": user["name"], "role": user["role"]}
        for user in api_response
    }
    
    print("Reshaped for fast lookup:")
    print(f"  User 102: {users_dict[102]}")
    print(f"  User 103: {users_dict[103]}")
    
    print("\n\n[9] CONFIGURATION OVERRIDES")
    print("-" * 70)
    
    default_config = {
        "debug": False,
        "timeout": 30,
        "retries": 3,
        "log_level": "INFO"
    }
    
    user_overrides = {
        "debug": True,
        "timeout": 60
    }
    
    # Merge configs (user overrides win)
    final_config = {
        key: user_overrides.get(key, default_value)
        for key, default_value in default_config.items()
    }
    
    print("Final configuration:")
    for key, value in final_config.items():
        overridden = key in user_overrides
        status = " (overridden)" if overridden else ""
        print(f"  {key}: {value}{status}")
    
    print("\n\n[10] PERFORMANCE METRICS CALCULATION")
    print("-" * 70)
    
    server_metrics = {
        "server1": {"requests": 1000, "errors": 10},
        "server2": {"requests": 1500, "errors": 45},
        "server3": {"requests": 800, "errors": 5},
    }
    
    # Calculate error rates
    error_rates = {
        server: (metrics["errors"] / metrics["requests"]) * 100
        for server, metrics in server_metrics.items()
    }
    
    print("Server error rates:")
    for server, rate in sorted(error_rates.items(), key=lambda x: x[1]):
        print(f"  {server}: {rate:.2f}%")
    
    print("\n" + "="*70)
    print("Dictionary Comprehension Syntax:")
    print("-" * 70)
    print("{key_expr: value_expr for item in iterable if condition}")
    print("\nCommon Patterns:")
    print("1. Transform values: {k: v*2 for k, v in dict.items()}")
    print("2. Filter items: {k: v for k, v in dict.items() if condition}")
    print("3. Swap key/value: {v: k for k, v in dict.items()}")
    print("4. From list: {item['id']: item for item in list}")
    print("\nBenefits:")
    print("✓ Concise dictionary creation")
    print("✓ Transform/filter in single expression")
    print("✓ Faster than loop + dict.update()")
    print("✓ Pythonic data transformation")
    print("="*70)


if __name__ == "__main__":
    main()