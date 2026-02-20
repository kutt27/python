"""
Error Log Analysis.
"""

from typing import List, Dict

def analyze_api_errors(error_logs: List[str]) -> Dict[str, int]:
    """
    Analyzes API error logs and counts error types.
    
    Args:
        error_logs: List of error log messages
    
    Returns:
        Dictionary of error type counts
    
    Real-world use case: Log analysis, error monitoring.
    """
    error_counts: Dict[str, int] = {}
    
    for log in error_logs:
        # Extract error type (simplified)
        if "Timeout" in log:
            error_counts["Timeout"] = error_counts.get("Timeout", 0) + 1
        elif "404" in log:
            error_counts["NotFound"] = error_counts.get("NotFound", 0) + 1
        elif "500" in log:
            error_counts["ServerError"] = error_counts.get("ServerError", 0) + 1
        else:
            error_counts["Other"] = error_counts.get("Other", 0) + 1
    
    return error_counts


def demonstrate_error_analysis() -> None:
    """
    Demonstrates log analysis by iterating over patterns.
    
    Real-world use case: Monitoring, observability.
    """
    logs = [
        "2024-12-05 ERROR: Timeout connecting to database",
        "2024-12-05 ERROR: 404 Not Found /api/users/999",
        "2024-12-05 ERROR: 500 Internal Server Error",
        "2024-12-05 ERROR: Timeout on external API call",
        "2024-12-05 ERROR: 404 Not Found /api/products/123",
    ]
    
    error_summary = analyze_api_errors(logs)
    print(f"\nAnalyzed {len(logs)} error logs:")
    for error_type, count in error_summary.items():
        print(f"  {error_type}: {count}")


if __name__ == "__main__":
    demonstrate_error_analysis()
