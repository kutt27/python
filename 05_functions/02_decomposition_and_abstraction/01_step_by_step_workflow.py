"""
Topic: Function Decomposition.

Breaking a complex task (like generating a report) into smaller, 
manageable steps with single responsibilities.
"""

from typing import Dict, List, Any

def fetch_user_data(user_id: int) -> Dict[str, Any]:
    """Abstraction: Hides database implementation details."""
    print(f"  → Fetching user {user_id}...")
    return {"id": user_id, "name": "Alice Smith", "email": "alice@example.com", "orders": [101, 102]}

def calculate_metrics(user_data: Dict) -> Dict[str, Any]:
    """Processes raw data into useful analytics."""
    print(f"  → Calculating metrics for {user_data['name']}...")
    return {"total_spent": 450.0, "tier": "VIP"}

def format_output(user_data: Dict, metrics: Dict) -> str:
    """Formats results for display."""
    return f"Report for {user_data['name']}: {metrics['tier']} Status"

def generate_report(user_id: int) -> str:
    """Orchestrates the workflow by calling smaller functions."""
    data = fetch_user_data(user_id)
    metrics = calculate_metrics(data)
    return format_output(data, metrics)

if __name__ == "__main__":
    report = generate_report(101)
    print(f"\nResult: {report}")
