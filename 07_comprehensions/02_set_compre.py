"""
Python Set Comprehensions
==========================

Topic: Set comprehensions for unique value extraction and deduplication

Real-World Applications:
- Removing duplicates from data
- Tag/keyword extraction
- Unique visitor tracking
- Feature set extraction
- Deduplication in ETL pipelines
"""

from typing import Set, List, Dict


def main() -> None:
    """Main function demonstrating set comprehensions."""
    print("="*70)
    print("SET COMPREHENSIONS".center(70))
    print("="*70)
    
    print("\n[1] BASIC DEDUPLICATION")
    print("-" * 70)
    
    # Remove duplicate user IDs
    user_ids_with_dupes = [101, 102, 101, 103, 102, 104, 101]
    
    # Set comprehension for unique values
    unique_ids = {user_id for user_id in user_ids_with_dupes}
    
    print(f"With duplicates: {user_ids_with_dupes}")
    print(f"Unique: {sorted(unique_ids)}")
    
    print("\n\n[2] TAG EXTRACTION - Blog/CMS System")
    print("-" * 70)
    
    blog_posts = [
        {"title": "Python Tutorial", "tags": ["python", "programming", "tutorial"]},
        {"title": "Web Development", "tags": ["web", "python", "javascript"]},
        {"title": "Machine Learning", "tags": ["python", "ml", "data"]},
    ]
    
    # Extract all unique tags
    all_unique_tags = {
        tag
        for post in blog_posts
        for tag in post["tags"]
    }
    
    print(f"All unique tags: {sorted(all_unique_tags)}")
    
    print("\n\n[3] FEATURE EXTRACTION FROM RECORDS")
    print("-" * 70)
    
    product_data = [
        {"name": "Laptop", "category": "Electronics", "features": ["wifi", "bluetooth", "usb-c"]},
        {"name": "Phone", "category": "Electronics", "features": ["wifi", "bluetooth", "5g"]},
        {"name": "Tablet", "category": "Electronics", "features": ["wifi", "bluetooth", "stylus"]},
    ]
    
    # Extract unique features across all products
    unique_features = {
        feature
        for product in product_data
        for feature in product["features"]
    }
    
    print(f"Unique features: {sorted(unique_features)}")
    
    print("\n\n[4] IP ADDRESS DEDUPLICATION - Network Logs")
    print("-" * 70)
    
    access_logs = [
        {"ip": "192.168.1.1", "endpoint": "/api/users"},
        {"ip": "10.0.0.5", "endpoint": "/api/products"},
        {"ip": "192.168.1.1", "endpoint": "/api/orders"},
        {"ip": "203.0.113.1", "endpoint": "/api/users"},
        {"ip": "10.0.0.5", "endpoint": "/api/products"},
    ]
    
    # Unique IPs that accessed the API
    unique_ips = {log["ip"] for log in access_logs}
    
    print(f"Unique IP addresses: {sorted(unique_ips)}")
    print(f"Total unique visitors: {len(unique_ips)}")
    
    print("\n\n[5] FILTERING WITH SET COMPREHENSION")
    print("-" * 70)
    
    # Extract unique error codes from logs
    error_logs = [
        {"code": 404, "message": "Not found"},
        {"code": 500, "message": "Server error"},
        {"code": 404, "message": "Not found"},
        {"code": 403, "message": "Forbidden"},
        {"code": 500, "message": "Server error"},
    ]
    
    # Unique error codes (4xx and 5xx only)
    unique_error_codes = {
        log["code"]
        for log in error_logs
        if log["code"] >= 400
    }
    
    print(f"Unique error codes: {sorted(unique_error_codes)}")
    
    print("\n\n[6] DOMAIN EXTRACTION FROM EMAILS")
    print("-" * 70)
    
    email_list = [
        "alice@example.com",
        "bob@company.org",
        "charlie@example.com",
        "diana@example.com",
        "eve@company.org",
    ]
    
    # Extract unique domains
    unique_domains = {
        email.split("@")[1]
        for email in email_list
        if "@" in email
    }
    
    print(f"Unique email domains: {sorted(unique_domains)}")
    
    print("\n\n[7] CASE-INSENSITIVE DEDUPLICATION")
    print("-" * 70)
    
    keywords = ["Python", "python", "PYTHON", "JavaScript", "javascript", "Java"]
    
    # Unique keywords (case-insensitive)
    unique_keywords = {keyword.lower() for keyword in keywords}
    
    print(f"Original (with case dupes): {keywords}")
    print(f"Unique (case-insensitive): {sorted(unique_keywords)}")
    
    print("\n\n[8] FILE EXTENSION EXTRACTION")
    print("-" * 70)
    
    file_list = [
        "document.pdf",
        "image.png",
        "report.pdf",
        "photo.jpg",
        "data.csv",
        "presentation.pdf",
        "chart.png",
    ]
    
    # Unique file extensions
    unique_extensions = {
        filename.split(".")[-1]
        for filename in file_list
        if "." in filename
    }
    
    print(f"Unique file types: {sorted(unique_extensions)}")
    
    print("\n\n[9] SET OPERATIONS - User Permissions")
    print("-" * 70)
    
    user_roles_db = [
        {"user": "alice", "roles": ["admin", "user", "manager"]},
        {"user": "bob", "roles": ["user", "viewer"]},
        {"user": "charlie", "roles": ["admin", "developer"]},
    ]
    
    # All unique roles in the system
    all_roles = {
        role
        for user_data in user_roles_db
        for role in user_data["roles"]
    }
    
    print(f"All roles in system: {sorted(all_roles)}")
    
    # Users with admin role
    admin_users = {
        user_data["user"]
        for user_data in user_roles_db
        if "admin" in user_data["roles"]
    }
    
    print(f"Admin users: {sorted(admin_users)}")
    
    print("\n\n[10] REAL-WORLD: DEPENDENCY ANALYSIS")
    print("-" * 70)
    
    # Code modules and their dependencies
    module_dependencies = {
        "api": ["database", "auth", "utils"],
        "auth": ["database", "utils"],
        "frontend": ["api", "utils"],
        "database": ["utils"],
    }
    
    # All unique dependencies
    all_dependencies = {
        dep
        for module_deps in module_dependencies.values()
        for dep in module_deps
    }
    
    print("All unique dependencies:")
    for dep in sorted(all_dependencies):
        # Count how many modules depend on it
        dependent_count = sum(
            1 for deps in module_dependencies.values()
            if dep in deps
        )
        print(f"  {dep}: used by {dependent_count} modules")
    
    print("\n" + "="*70)
    print("Set Comprehension Syntax:")
    print("-" * 70)
    print("{expression for item in iterable if condition}")
    print("\nKey Differences from List Comprehension:")
    print("• Uses curly braces {} instead of []")
    print("• Automatically removes duplicates")
    print("• No guaranteed order (sets are unordered)")
    print("• Faster membership testing: item in set")
    print("\nWhen to Use:")
    print("✓ Need unique values only")
    print("✓ Removing duplicates from data")
    print("✓ Extracting unique features/tags")
    print("✓ Set operations (union, intersection, difference)")
    print("="*70)


if __name__ == "__main__":
    main()