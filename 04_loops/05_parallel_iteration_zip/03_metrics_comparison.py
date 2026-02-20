"""
Performance Metrics Comparison.
"""

from typing import List

def compare_metrics_over_time(
    dates: List[str],
    api_requests: List[int],
    errors: List[int],
    response_times: List[float]
) -> None:
    """
    Compares multiple metrics across time periods.
    
    Args:
        dates: Date strings
        api_requests: Request counts
        errors: Error counts
        response_times: Average response times
    
    Real-world use case: Performance monitoring dashboards.
    """
    print("\nPerformance Metrics Over Time")
    print("-" * 70)
    print(f"{'Date':12} | {'Requests':>8} | {'Errors':>6} | {'Avg Response':>12}")
    print("-" * 70)
    
    for date, requests, error_count, avg_time in zip(dates, api_requests, errors, response_times):
        print(f"{date:12} | {requests:>8} | {error_count:>6} | {avg_time:>10.0f}ms")


def demonstrate_metrics() -> None:
    """
    Demonstrates metrics comparison.
    """
    dates = ["2024-12-01", "2024-12-02", "2024-12-03", "2024-12-04"]
    requests_per_day = [10000, 12000, 11500, 13000]
    errors_per_day = [50, 120, 80, 95]
    avg_response_times = [150, 180, 165, 155]
    
    compare_metrics_over_time(dates, requests_per_day, errors_per_day, avg_response_times)


if __name__ == "__main__":
    demonstrate_metrics()
