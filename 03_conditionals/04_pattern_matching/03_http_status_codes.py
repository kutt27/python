"""
HTTP Status Codes logic.
"""

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


def demonstrate_http_status_codes() -> None:
    """
    Demonstrates status code categorization with guard conditions.
    
    Real-world use case: HTTP clients, monitoring systems.
    """
    status_codes = [200, 201, 301, 404, 429, 500, 503, 418, 226]
    
    for code in status_codes:
        category = categorize_http_status(code)
        print(f"  {code:3} -> {category}")


if __name__ == "__main__":
    demonstrate_http_status_codes()
