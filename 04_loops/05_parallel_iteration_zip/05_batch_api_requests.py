"""
Batch API Requests creation.
"""

from typing import List, Dict

def create_api_request_batch(
    endpoints: List[str],
    methods: List[str],
    payloads: List[Dict]
) -> List[Dict]:
    """
    Creates batch of API requests from separate lists.
    
    Args:
        endpoints: API endpoints
        methods: HTTP methods
        payloads: Request payloads
    
    Returns:
        List of request dictionaries
    
    Real-world use case: Bulk API operations, batch processing.
    """
    requests = []
    
    for endpoint, method, payload in zip(endpoints, methods, payloads):
        request = {
            "url": endpoint,
            "method": method,
            "data": payload
        }
        requests.append(request)
    
    return requests


def demonstrate_batch_requests() -> None:
    """
    Demonstrates batch API request creation.
    """
    api_endpoints = ["/users/1", "/users/2", "/users/3"]
    http_methods = ["GET", "PUT", "DELETE"]
    request_payloads = [{}, {"name": "Updated"}, {}]
    
    batch_requests = create_api_request_batch(api_endpoints, http_methods, request_payloads)
    
    print("\nBatch API requests:")
    for i, req in enumerate(batch_requests, 1):
        print(f"  Request {i}: {req['method']} {req['url']}")
        if req['data']:
            print(f"    Data: {req['data']}")


if __name__ == "__main__":
    demonstrate_batch_requests()
