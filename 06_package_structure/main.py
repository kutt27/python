"""
Python Package Structure - Main Application
============================================

This file demonstrates different ways to import from packages and modules.

Topics Covered:
1. Absolute imports (from package.module import ...)
2. Package-level imports (from package import ...)
3. Star imports (from package import *)
4. Module aliases (import module as alias)
5. Relative imports (from . import ...)

Real-World Application:
- Organizing large applications into packages
- Creating reusable libraries
- Managing dependencies between modules
"""

# =============================================================================
# IMPORT PATTERNS
# =============================================================================

print("="*70)
print("PYTHON PACKAGE STRUCTURE & IMPORTS".center(70))
print("="*70)

# Pattern 1: Import specific classes from submodules
print("\n[1] SPECIFIC IMPORTS FROM SUBMODULES")
print("-" * 70)

from api.auth import APIAuthenticator, create_auth_headers
from api.client import HTTPClient
from utils.helpers import validate_email, format_response, paginate_results

print("✓ Imported: APIAuthenticator, HTTPClient, utilities")

# Pattern 2: Import entire modules
print("\n[2] IMPORT ENTIRE MODULES")
print("-" * 70)

import api.auth as auth_module
import utils.helpers as helpers

print("✓ Imported modules with aliases")
print(f"  api.auth module: {auth_module}")
print(f"  utils.helpers module: {helpers}")

# Pattern 3: Package-level imports (uses __init__.py)
print("\n[3] PACKAGE-LEVEL IMPORTS")
print("-" * 70)

# This works because __init__.py exports these
from api import APIAuthenticator as Auth, HTTPClient as Client
from utils import validate_email as check_email

print("✓ Imported from package level (via __init__.py)")

# =============================================================================
# USAGE EXAMPLES
# =============================================================================

print("\n\n" + "="*70)
print("USAGE EXAMPLES".center(70))
print("="*70)

# Example 1: Authentication
print("\n[1] API AUTHENTICATION")
print("-" * 70)

authenticator = APIAuthenticator(api_key="demo_key_123", api_secret="demo_secret_456")

try:
    token = authenticator.authenticate()
    print(f"✓ Authentication successful")
    print(f"  Token: {token[:30]}...")
    
    headers = create_auth_headers(token)
    print(f"  Headers: {headers}")

except Exception as e:
    print(f"✗ Authentication failed: {e}")

# Example 2: HTTP Client
print("\n\n[2] HTTP CLIENT USAGE")
print("-" * 70)

client = HTTPClient(base_url="https://api.example.com")

# GET request
print("\nGET Request:")
response = client.get("/users", params={"limit": 10})
print(f"Response: {response}")

# POST request
print("\nPOST Request:")
new_user = {"name": "Alice", "email": "alice@example.com"}
response = client.post("/users", data=new_user)
print(f"Response: {response}")

# Example 3: Utilities
print("\n\n[3] UTILITY FUNCTIONS")
print("-" * 70)

# Email validation
test_emails = ["valid@example.com", "invalid.email", "test@domain.io"]

print("\nEmail Validation:")
for email in test_emails:
    is_valid = validate_email(email)
    status = "✓ Valid" if is_valid else "✗ Invalid"
    print(f"  {status}: {email}")

# Response formatting
print("\nResponse Formatting:")
success_response = format_response({"user_id": 123}, status="success")
error_response = format_response(None, status="error", error="User not found")

print(f"  Success: {success_response}")
print(f"  Error: {error_response}")

# Pagination
print("\nPagination:")
items = list(range(1, 51))  # 50 items
page_1 = paginate_results(items, page=1, page_size=10)

print(f"  Page 1 items: {page_1['items'][:5]}... (showing first 5)")
print(f"  Pagination: {page_1['pagination']}")

# =============================================================================
# IMPORT BEST PRACTICES
# =============================================================================

print("\n\n" + "="*70)
print("IMPORT BEST PRACTICES".center(70))
print("="*70)

print("""
1. ABSOLUTE IMPORTS (Recommended):
   from api.auth import APIAuthenticator
   from utils.helpers import validate_email

2. PACKAGE-LEVEL IMPORTS:
   from api import APIAuthenticator  # Works if exported in __init__.py
   
3. MODULE ALIASES:
   import api.client as client  # For namespacing

4. AVOID STAR IMPORTS IN PRODUCTION:
   from api import *  # Use sparingly, makes code less clear

5. RELATIVE IMPORTS (within packages):
   from . import auth  # Same package
   from .. import utils  # Parent package
   from .auth import APIAuthenticator  # Module in same package

PACKAGE STRUCTURE:
06_package_structure/
├── __init__.py              (optional: makes directory a package)
├── main.py                  (application entry point)
├── api/                     (subpackage)
│   ├── __init__.py         (exports: APIAuthenticator, HTTPClient)
│   ├── auth.py             (authentication module)
│   └── client.py           (HTTP client module)
└── utils/                   (subpackage)
    ├── __init__.py         (exports utility functions)
    └── helpers.py          (utility functions)

KEY CONCEPTS:
• __init__.py: Makes directory a package, controls exports
• __all__: Defines what 'from package import *' imports
• Subpackages: Nested packages for organization
• Module: Single .py file
• Package: Directory with __init__.py

REAL-WORLD USE CASES:
✓ API clients (requests, httpx patterns)
✓ Web frameworks (Flask, FastAPI structure)
✓ Data processing pipelines
✓ ML model packages
✓ CLI tools with subcommands
""")

print("="*70)
print("Package structure examples completed successfully!")
print("="*70)
