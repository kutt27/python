"""
Status Code Analytics.
"""

from typing import List, Dict, Any

def count_status_codes(access_logs: List[Dict[str, Any]]) -> Dict[int, int]:
    """
    Counts HTTP status codes from access logs.
    
    Args:
        access_logs: List of access log entries
    
    Returns:
        Dictionary of status code counts
    
    Real-world use case: Web server analytics.
    """
    status_counts: Dict[int, int] = {}
    
    for log_entry in access_logs:
        status = log_entry.get("status", 0)
        status_counts[status] = status_counts.get(status, 0) + 1
    
    return status_counts


def demonstrate_analytics() -> None:
    """
    Demonstrates status code analytics.
    """
    logs = [
        {"path": "/users", "status": 200},
        {"path": "/products", "status": 200},
        {"path": "/missing", "status": 404},
        {"path": "/api/data", "status": 500},
        {"path": "/health", "status": 200},
    ]
    
    status_summary = count_status_codes(logs)
    print("\nHTTP Status Code Summary:")
    for status, count in sorted(status_summary.items()):
        print(f"  {status}: {count} requests")


if __name__ == "__main__":
    demonstrate_analytics()
