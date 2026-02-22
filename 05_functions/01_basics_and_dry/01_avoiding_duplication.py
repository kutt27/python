"""
Topic: Function basics and avoiding code duplication.

DRY Principle: Don't Repeat Yourself - instead of duplicating logging code 
throughout the application, centralize it in a reusable function.
"""

from datetime import datetime

def log_api_request(method: str, endpoint: str, status_code: int) -> None:
    """
    Logs API request information centrally.
    
    Real-world use case: API request logging, monitoring.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {method} {endpoint} - {status_code}")

# Example Usage:
if __name__ == "__main__":
    # Same logging function used for all endpoints
    log_api_request("GET", "/api/users", 200)
    log_api_request("POST", "/api/orders", 201)
    log_api_request("DELETE", "/api/cache", 204)
    log_api_request("GET", "/api/products", 404)
