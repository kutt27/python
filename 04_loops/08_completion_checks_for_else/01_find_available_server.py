"""
Find Available Server.
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


def demonstrate_server_search() -> None:
    """
    Demonstrates finding available server.
    """
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


if __name__ == "__main__":
    demonstrate_server_search()
