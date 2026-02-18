"""
API Routing logic.
"""

from typing import Dict, Any
from enum import Enum

class HTTPMethod(Enum):
    """HTTP request methods."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


def route_api_request(method: str, endpoint: str, data: Dict[str, Any] = None) -> str:
    """
    Routes API requests using pattern matching.
    
    Args:
        method: HTTP method
        endpoint: API endpoint path
        data: Request data
    
    Returns:
        Response message
    
    Real-world use case: API routing, request handling.
    """
    match (method, endpoint):
        case ("GET", "/users"):
            return "📋 Fetching user list"
        
        case ("GET", "/users" | "/user"):  # Pattern alternatives
            return "📋 Fetching single user"
        
        case ("POST", "/users"):
            return f"✅ Creating new user: {data.get('name', 'Unknown')}"
        
        case ("PUT" | "PATCH", "/users"):
            return f"📝 Updating user: {data.get('id', 'Unknown')}"
        
        case ("DELETE", "/users"):
            return f"🗑 Deleting user: {data.get('id', 'Unknown')}"
        
        case ("GET", "/health"):
            return "✓ Service is healthy"
        
        case _:
            return f"❌ Unknown route: {method} {endpoint}"


def demonstrate_api_routing() -> None:
    """
    Demonstrates API request routing using pattern matching.
    
    Real-world use case: Web frameworks, API development.
    """
    requests = [
        ("GET", "/users", {}),
        ("POST", "/users", {"name": "Alice"}),
        ("DELETE", "/users", {"id": 123}),
        ("GET", "/health", {}),
        ("POST", "/unknown", {}),
    ]
    
    for method, endpoint, data in requests:
        result = route_api_request(method, endpoint, data)
        print(f"{method:6} {endpoint:15} -> {result}")


if __name__ == "__main__":
    demonstrate_api_routing()
