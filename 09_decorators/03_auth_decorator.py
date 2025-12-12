"""
Python Decorators: Authentication & Authorization
==================================================

Topic: Access control decorators, permission checking, role-based access

Real-World Applications:
- API endpoint protection
- Role-based access control (RBAC)
- Permission validation
- Admin-only operations
- User session management
"""

from functools import wraps
from typing import Callable, Dict, List, Optional


# Simulated user database and session
USERS_DB = {
    "alice": {"user_id": 101, "role": "admin", "permissions": ["read", "write", "delete"]},
    "bob": {"user_id": 102, "role": "user", "permissions": ["read", "write"]},
    "charlie": {"user_id": 103, "role": "viewer", "permissions": ["read"]},
}

CURRENT_USER: Optional[Dict] = None


def login(username: str) -> bool:
    """Simulates user login."""
    global CURRENT_USER
    
    if username in USERS_DB:
        CURRENT_USER = {"username": username, **USERS_DB[username]}
        print(f"✓ Logged in as: {username} ({CURRENT_USER['role']})")
        return True
    
    print(f"✗ Login failed: unknown user '{username}'")
    return False


def logout():
    """Simulates user logout."""
    global CURRENT_USER
    CURRENT_USER = None
    print("Logged out")


def require_authentication(func: Callable) -> Callable:
    """
    Requires user to be authenticated.
    
    Real-world use case: Protected API endpoints.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if CURRENT_USER is None:
            print(f"❌ Access denied: Authentication required for {func.__name__}()")
            return None
        
        return func(*args, **kwargs)
    
    return wrapper


def require_role(required_role: str):
    """
    Decorator factory: requires specific role.
    
    Args:
        required_role: Required role name
    
    Real-world use case: Role-based access control.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_USER is None:
                print(f"❌ Access denied: Authentication required")
                return None
            
            if CURRENT_USER.get("role") != required_role:
                print(f"❌ Access denied: '{required_role}' role required")
                print(f"   Your role: '{CURRENT_USER.get('role')}'")
                return None
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator


def require_permission(permission: str):
    """
    Decorator factory: requires specific permission.
    
    Args:
        permission: Required permission
    
    Real-world use case: Fine-grained access control.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_USER is None:
                print(f"❌ Access denied: Authentication required")
                return None
            
            user_permissions = CURRENT_USER.get("permissions", [])
            
            if permission not in user_permissions:
                print(f"❌ Access denied: '{permission}' permission required")
                print(f"   Your permissions: {user_permissions}")
                return None
            
            print(f"✓ Permission check passed: {permission}")
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator


def require_any_role(*roles: str):
    """
    Requires user to have ANY of the specified roles.
    
    Args:
        *roles: Allowed roles
    
    Real-world use case: Multi-role access.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_USER is None:
                print(f"❌ Access denied: Authentication required")
                return None
            
            user_role = CURRENT_USER.get("role")
            
            if user_role not in roles:
                print(f"❌ Access denied: Must be one of: {roles}")
                print(f"   Your role: '{user_role}'")
                return None
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator


def log_access(func: Callable) -> Callable:
    """
    Logs access attempts.
    
    Real-world use case: Security auditing, access logs.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = CURRENT_USER.get("username") if CURRENT_USER else "anonymous"
        print(f"📋 Access log: {username} → {func.__name__}()")
        
        result = func(*args, **kwargs)
        
        if result is not None:
            print(f"📋 Access granted to {func.__name__}()")
        
        return result
    
    return wrapper


# Protected endpoints/functions

@require_authentication
def view_profile() -> dict:
    """View user profile (authentication required)."""
    return {
        "username": CURRENT_USER["username"],
        "role": CURRENT_USER["role"]
    }


@require_role("admin")
def delete_user(user_id: int) -> bool:
    """Delete user (admin only)."""
    print(f"  Deleting user {user_id}...")
    return True


@require_permission("write")
def create_post(title: str, content: str) -> dict:
    """Create post (write permission required)."""
    return {
        "title": title,
        "author": CURRENT_USER["username"],
        "content": content
    }


@require_permission("delete")
def delete_post(post_id: int) -> bool:
    """Delete post (delete permission required)."""
    print(f"  Deleting post {post_id}...")
    return True


@require_any_role("admin", "user")
def update_settings(setting: str, value: str) -> bool:
    """Update settings (admin or user role)."""
    print(f"  Updated {setting} = {value}")
    return True


@log_access
@require_role("admin")
def access_admin_panel() -> dict:
    """Access admin panel (admin only, logged)."""
    return {"panel": "admin", "features": ["users", "settings", "reports"]}


def main() -> None:
    """Main function demonstrating authentication decorators."""
    print("="*70)
    print("AUTHENTICATION & AUTHORIZATION DECORATORS".center(70))
    print("="*70)
    
    print("\n[1] REQUIRE AUTHENTICATION")
    print("-" * 70)
    
    # Try without authentication
    print("Attempting to view profile (not logged in):")
    view_profile()
    
    # Login and try again
    login("alice")
    print("\nAttempting to view profile (logged in as alice):")
    profile = view_profile()
    if profile:
        print(f"  Profile: {profile}")
    
    logout()
    
    print("\n\n[2] ROLE-BASED ACCESS CONTROL")
    print("-" * 70)
    
    # Admin role
    print("Testing admin-only function:")
    login("alice")  # alice is admin
    delete_user(999)
    logout()
    
    print("\nNon-admin trying admin function:")
    login("bob")  # bob is user, not admin
    delete_user(999)
    logout()
    
    print("\n\n[3] PERMISSION-BASED ACCESS")
    print("-" * 70)
    
    # User with write permission
    login("bob")
    print("User with 'write' permission:")
    post = create_post("My Post", "Content here")
    if post:
        print(f"  Created: {post['title']}")
    
    # User without delete permission
    print("\nUser without 'delete' permission:")
    delete_post(123)
    logout()
    
    # Admin with delete permission
    login("alice")
    print("\nAdmin with 'delete' permission:")
    deleted = delete_post(123)
    logout()
    
    print("\n\n[4] MULTI-ROLE ACCESS")
    print("-" * 70)
    
    # Viewer (not admin or user)
    login("charlie")
    print("Viewer trying user/admin function:")
    update_settings("theme", "dark")
    logout()
    
    # User (allowed)
    login("bob")
    print("\nUser trying user/admin function:")
    update_settings("theme", "dark")
    logout()
    
    print("\n\n[5] ACCESS LOGGING")
    print("-" * 70)
    
    login("alice")
    print("Admin accessing admin panel (with logging):")
    panel = access_admin_panel()
    if panel:
        print(f"  Panel features: {panel['features']}")
    logout()
    
    print("\n\n[6] STACKED ACCESS CONTROLS")
    print("-" * 70)
    
    @log_access
    @require_permission("delete")
    @require_role("admin")
    def critical_operation():
        """Operation with multiple security layers."""
        print("  Executing critical operation...")
        return "Success"
    
    login("bob")  # User, has delete permission but not admin role
    print("User with permission but wrong role:")
    critical_operation()
    logout()
    
    login("alice")  # Admin with all permissions
    print("\nAdmin with all requirements:")
    result = critical_operation()
    logout()
    
    print("\n" + "="*70)
    print("Authentication/Authorization Best Practices:")
    print("-" * 70)
    print("• Always check authentication first")
    print("• Fail securely (deny by default)")
    print("• Log access attempts for security auditing")
    print("• Use fine-grained permissions over roles when possible")
    print("• Stack decorators for defense in depth")
    print("\nCommon Patterns:")
    print("✓ @require_authentication - Must be logged in")
    print("✓ @require_role('admin') - Specific role required")
    print("✓ @require_permission('write') - Specific permission")
    print("✓ @require_any_role('admin', 'user') - Multiple roles allowed")
    print("✓ @log_access - Audit trail")
    print("="*70)


if __name__ == "__main__":
    main()