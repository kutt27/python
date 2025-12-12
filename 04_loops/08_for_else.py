"""
Python For-Else: Loop Completion Handling
==========================================

Topic: for-else clause for loop completion detection

Real-World Applications:
- Search operations result handling
- Validation with fallback
- Resource allocation with failure handling
- Authentication attempts
- Failover logic
"""

from typing import List, Optional, Dict


def find_available_server(servers: List[Dict]) -> Optional[str]:
    """
    Finds first available server, uses else for failure handling.
    
    Args:
        servers: List of server dictionaries
    
    Returns:
        Server name if available, None otherwise
    
    Real-world use case: Load balancing, failover systems.
    """
    print("\nSearching for available server")
    print("-" * 60)
    
    for server in servers:
        name = server['name']
        available = server.get('available', False)
        
        print(f"  Checking {name}... ", end="")
        
        if available:
            print("✓ AVAILABLE")
            return name  # Found available server, break out
        else:
            print("✗ Busy")
    
    else:
        # This runs ONLY if loop completed without break
        print("\n🛑 NO AVAILABLE SERVERS FOUND")
        return None


def authenticate_user(username: str, password: str, auth_methods: List[str]) -> tuple[bool, Optional[str]]:
    """
    Tries multiple authentication methods.
    
    Args:
        username: Username
        password: Password
        auth_methods: List of auth methods to try
    
    Returns:
        Tuple of (success, method_used)
    
    Real-world use case: Multi-factor authentication, auth fallback.
    """
    print(f"\nTrying authentication for user: {username}")
    print("-" * 60)
    
    for method in auth_methods:
        print(f"  Attempting {method}... ", end="")
        
        # Simulate authentication (only OAuth succeeds in this example)
        if method == "OAuth":
            print("✓ SUCCESS")
            return (True, method)
        else:
            print("✗ Failed")
    
    else:
        # No authentication method succeeded
        print("\n🚫 ALL AUTHENTICATION METHODS FAILED")
        return (False, None)


def allocate_instance(required_memory: int, available_instances: List[Dict]) -> Optional[str]:
    """
    Allocates cloud instance with sufficient resources.
    
    Args:
        required_memory: Required memory in GB
        available_instances: List of instance dictionaries
    
    Returns:
        Instance ID if allocated, None otherwise
    
    Real-world use case: Cloud resource allocation, auto-scaling.
    """
    print(f"\nAllocating instance with {required_memory}GB memory")
    print("-" * 60)
    
    for instance in available_instances:
        instance_id = instance['id']
        memory = instance['memory_gb']
        
        print(f"  Instance {instance_id} ({memory}GB)... ", end="")
        
        if memory >= required_memory:
            print("✓ ALLOCATED")
            return instance_id
        else:
            print("✗ Insufficient memory")
    
    else:
        print("\n⚠ NO SUITABLE INSTANCE FOUND - Need to scale up")
        return None


def validate_config_keys(config: Dict, required_keys: List[str]) -> bool:
    """
    Validates all required configuration keys exist.
    
    Args:
        config: Configuration dictionary
        required_keys: List of required keys
    
    Returns:
        True if all keys present, False otherwise
    
    Real-world use case: Application startup validation.
    """
    print(f"\nValidating configuration ({len(required_keys)} required keys)")
    print("-" * 60)
    
    for key in required_keys:
        print(f"  Checking '{key}'... ", end="")
        
        if key not in config:
            print(f"✗ MISSING")
            return False  # Early exit - validation failed
        else:
            print("✓ Found")
    
    else:
        # All keys validated successfully
        print("\n✅ ALL REQUIRED KEYS PRESENT")
        return True


def find_primary_contact(contacts: List[Dict[str, any]]) -> Optional[Dict]:
    """
    Finds primary contact in contact list.
    
    Args:
        contacts: List of contact dictionaries
    
    Returns:
        Primary contact if found, None otherwise
    
    Real-world use case: CRM systems, notification dispatch.
    """
    print("\nSearching for primary contact")
    print("-" * 60)
    
    for contact in contacts:
        name = contact.get('name')
        is_primary = contact.get('is_primary', False)
        
        print(f"  {name}: ", end="")
        
        if is_primary:
            print("✓ PRIMARY CONTACT FOUND")
            return contact
        else:
            print("Secondary")
    
    else:
        print("\n⚠ NO PRIMARY CONTACT - Using first contact as fallback")
        return contacts[0] if contacts else None


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("FOR-ELSE: LOOP COMPLETION HANDLING".center(70))
    print("="*70)
    
    print("\n[1] FIND AVAILABLE SERVER")
    print("-" * 70)
    
    servers = [
        {"name": "server-01", "available": False},
        {"name": "server-02", "available": False},
        {"name": "server-03", "available": True},
        {"name": "server-04", "available": True},
    ]
    
    server = find_available_server(servers)
    if server:
        print(f"\n→ Routing request to: {server}")
    else:
        print("\n→ All servers busy - request queued")
    
    print("\n\n[2] AUTHENTICATION METHODS")
    print("-" * 70)
    
    methods = ["LDAP", "SAML", "OAuth", "Certificate"]
    success, method = authenticate_user("alice", "password123", methods)
    
    if success:
        print(f"\n→ User authenticated via {method}")
    else:
        print("\n→ Access denied")
    
    print("\n\n[3] CLOUD INSTANCE ALLOCATION")
    print("-" * 70)
    
    instances = [
        {"id": "i-001", "memory_gb": 4},
        {"id": "i-002", "memory_gb": 8},
        {"id": "i-003", "memory_gb": 16},
    ]
    
    allocated = allocate_instance(required_memory=12, available_instances=instances)
    
    if allocated:
        print(f"\n→ Using instance: {allocated}")
    else:
        print("\n→ Triggering auto-scaling to create larger instance")
    
    print("\n\n[4] CONFIGURATION VALIDATION")
    print("-" * 70)
    
    app_config = {
        "database_url": "postgres://localhost/db",
        "api_key": "abc123",
        "redis_url": "redis://localhost:6379"
    }
    
    required = ["database_url", "api_key", "redis_url"]
    is_valid = validate_config_keys(app_config, required)
    
    if is_valid:
        print("\n→ Starting application...")
    else:
        print("\n→ Cannot start - fix configuration and retry")
    
    print("\n\n[5] PRIMARY CONTACT SEARCH")
    print("-" * 70)
    
    contact_list = [
        {"name":"Alice", "email": "alice@example.com", "is_primary": False},
        {"name": "Bob", "email": "bob@example.com", "is_primary": False},
        {"name": "Charlie", "email": "charlie@example.com", "is_primary": False},
    ]
    
    primary = find_primary_contact(contact_list)
    if primary:
        print(f"\n→ Sending notification to: {primary.get('name')}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. for-else: else block runs if loop completes without break")
    print("2. Useful for 'search-and-handle-not-found' patterns")
    print("3. Cleaner than flag variables (found = True)")
    print("4. Also works with while loops")
    print("5. Think: 'else' = 'if loop not broken'")
    print("="*70)


if __name__ == "__main__":
    main()