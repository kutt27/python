"""
Python Conditionals: Pattern Matching (Python 3.10+)
====================================================

Topic: match/case statements for structural pattern matching

Real-World Applications:
- HTTP request routing
- Command parsing in CLI tools
- State machine implementations
- Protocol message handling
- API endpoint versioning
"""

from typing import Dict, Any, List
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


def parse_cli_command(command: List[str]) -> str:
    """
    Parses CLI commands using pattern matching.
    
    Args:
        command: List of command parts
    
    Returns:
        Command result
    
    Real-world use case: CLI tool command parsing, task automation.
    """
    match command:
        # deploy command with environment
        case ["deploy", env] if env in ["dev", "staging", "production"]:
            return f"🚀 Deploying to {env}"
        
        # deploy without environment
        case ["deploy"]:
            return "⚠ Environment required: deploy <dev|staging|production>"
        
        # backup with database name
        case ["backup", "database", db_name]:
            return f"💾 Backing up database: {db_name}"
        
        # logs command with optional service
        case ["logs", service, *options]:
            opts_str = f" with options: {options}" if options else ""
            return f"📜 Showing logs for {service}{opts_str}"
        
        # scale command
        case ["scale", service, count] if count.isdigit():
            return f"📊 Scaling {service} to {count} instances"
        
        case ["help" | "--help" | "-h"]:
            return "ℹ Available commands: deploy, backup, logs, scale"
        
        case _:
            return f"❌ Unknown command: {' '.join(command)}"


def categorize_http_status(status_code: int) -> str:
    """
    Categorizes HTTP status codes using pattern matching.
    
    Args:
        status_code: HTTP status code
    
    Returns:
        Category and description
    
    Real-world use case: HTTP client error handling, monitoring.
    """
    match status_code:
        # Success responses (2xx)
        case 200:
            return "✅ OK - Request succeeded"
        case 201:
            return "✅ Created - Resource created successfully"
        case 204:
            return "✅ No Content - Request succeeded, no response body"
        
        # Redirection (3xx)
        case 301:
            return "↪ Moved Permanently - Resource moved"
        case 302 | 307:
            return "↪ Temporary Redirect"
        
        # Client errors (4xx)
        case 400:
            return "❌ Bad Request - Invalid request format"
        case 401:
            return "🔒 Unauthorized - Authentication required"
        case 403:
            return "🚫 Forbidden - Access denied"
        case 404:
            return "🔍 Not Found - Resource not found"
        case 429:
            return "⏱  Too Many Requests - Rate limited"
        
        # Server errors (5xx)
        case 500:
            return "💥 Internal Server Error"
        case 502:
            return "🚧 Bad Gateway - Upstream server error"
        case 503:
            return "🔧 Service Unavailable - Server overloaded"
        
        # Range patterns
        case code if 200 <= code < 300:
            return f"✅ Success ({code})"
        case code if 400 <= code < 500:
            return f"❌ Client Error ({code})"
        case code if 500 <= code < 600:
            return f"💥 Server Error ({code})"
        
        case _:
            return f"❓ Unknown status code: {status_code}"


def process_message(message: Dict[str, Any]) -> str:
    """
    Processes different message types using pattern matching.
    
    Args:
        message: Message dictionary with type and data
    
    Returns:
        Processing result
    
    Real-world use case: Message queue processing, event handling.
    """
    match message:
        # User registration event
        case {"type": "user.registered", "email": email, "user_id": uid}:
            return f"📧 Send welcome email to {email} (User: {uid})"
        
        # Order placed event
        case {"type": "order.placed", "order_id": oid, "amount": amount}:
            return f"💳 Process payment for order {oid}: ${amount}"
        
        # Payment successful
        case {"type": "payment.success", "transaction_id": tid}:
            return f"✅ Payment confirmed: {tid}"
        
        # Error event
        case {"type": "error", "service": service, "message": msg}:
            return f"🚨 Alert: {service} error - {msg}"
        
        # Health check
        case {"type": "health_check"}:
            return "✓ Service responding"
        
        case _:
            return f"⚠ Unknown message type: {message.get('type', 'none')}"


def determine_deployment_strategy(config: Dict[str, Any]) -> str:
    """
    Determines deployment strategy based on configuration.
    
    Args:
        config: Deployment configuration
    
    Returns:
        Deployment strategy description
    
    Real-world use case: CI/CD pipeline configuration, deployment automation.
    """
    match config:
        # Blue-green deployment
        case {"strategy": "blue-green", "environment": env}:
            return f"🔵🟢 Blue-green deployment to {env}"
        
        # Canary deployment with percentage
        case {"strategy": "canary", "percentage": pct} if 0 < pct <= 100:
            return f"🐤 Canary deployment: {pct}% traffic"
        
        # Rolling deployment
        case {"strategy": "rolling", "batch_size": size}:
            return f"🔄 Rolling deployment: {size} instances at a time"
        
        # Feature flag deployment
        case {"strategy": "feature-flag", "flag": flag_name, "enabled": enabled}:
            status = "enabled" if enabled else "disabled"
            return f"🚩 Feature flag '{flag_name}' {status}"
        
        case _:
            return "📦 Standard deployment (all-at-once)"



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


def demonstrate_cli_parsing() -> None:
    """
    Demonstrates CLI command parsing with list patterns.
    
    Real-world use case: Terminal applications, automation tools.
    """
    commands = [
        ["deploy", "production"],
        ["backup", "database", "users_db"],
        ["logs", "api-service", "--follow", "--tail=100"],
        ["scale", "web-app", "5"],
        ["help"],
        ["unknown", "command"],
    ]
    
    for cmd in commands:
        result = parse_cli_command(cmd)
        cmd_str = " ".join(cmd)
        print(f"  {cmd_str:35} -> {result}")


def demonstrate_http_status_codes() -> None:
    """
    Demonstrates status code categorization with guard conditions.
    
    Real-world use case: HTTP clients, monitoring systems.
    """
    status_codes = [200, 201, 301, 404, 429, 500, 503, 418, 226]
    
    for code in status_codes:
        category = categorize_http_status(code)
        print(f"  {code:3} -> {category}")


def demonstrate_message_processing() -> None:
    """
    Demonstrates dictionary pattern matching for event handling.
    
    Real-world use case: Message queues, microservices.
    """
    messages = [
        {"type": "user.registered", "email": "alice@example.com", "user_id": 101},
        {"type": "order.placed", "order_id": "ORD-123", "amount": 99.99},
        {"type": "payment.success", "transaction_id": "TXN-456"},
        {"type": "error", "service": "payment-api", "message": "Connection timeout"},
        {"type": "health_check"},
        {"type": "unknown.event"},
    ]
    
    for msg in messages:
        result = process_message(msg)
        print(f"  {result}")


def demonstrate_deployment_strategies() -> None:
    """
    Demonstrates strategy selection using structural matching.
    
    Real-world use case: CI/CD pipeline automation.
    """
    deployments = [
        {"strategy": "blue-green", "environment": "production"},
        {"strategy": "canary", "percentage": 10},
        {"strategy": "rolling", "batch_size": 3},
        {"strategy": "feature-flag", "flag": "new-ui", "enabled": True},
        {"strategy": "manual"},
    ]
    
    for config in deployments:
        strategy = determine_deployment_strategy(config)
        print(f"  {strategy}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PATTERN MATCHING: match/case (Python 3.10+)".center(70))
    print("="*70)
    
    print("\n[1] API REQUEST ROUTING")
    print("-" * 70)
    demonstrate_api_routing()
    
    print("\n\n[2] CLI COMMAND PARSING")
    print("-" * 70)
    demonstrate_cli_parsing()
    
    print("\n\n[3] HTTP STATUS CODE CATEGORIZATION")
    print("-" * 70)
    demonstrate_http_status_codes()
    
    print("\n\n[4] MESSAGE QUEUE PROCESSING")
    print("-" * 70)
    demonstrate_message_processing()
    
    print("\n\n[5] DEPLOYMENT STRATEGY SELECTION")
    print("-" * 70)
    demonstrate_deployment_strategies()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. match/case provides structural pattern matching (Python 3.10+)")
    print("2. Patterns can match values, types, and structures")
    print("3. Use guards (if conditions) for additional filtering")
    print("4. _ is the wildcard pattern (matches anything)")
    print("5. More readable than long if/elif chains for complex matching")
    print("="*70)


if __name__ == "__main__":
    main()