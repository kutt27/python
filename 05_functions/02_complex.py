"""
Python Functions: Decomposition and Abstraction
================================================

Topic: Breaking complex logic into smaller functions, abstraction layers

Real-World Applications:
- ETL pipeline orchestration
- Multi-step data processing
- API integration workflows
- Report generation systems
- Microservice orchestration
"""

from typing import Dict, List, Any
from datetime import datetime


def fetch_user_data(user_id: int) -> Dict[str, Any]:
    """
    Fetches user data from database.
    
    Abstraction: Hides database implementation details.
    
    Args:
        user_id: User identifier
    
    Returns:
        User data dictionary
    
    Real-world use case: Database abstraction layer.
    """
    print(f"  → Fetching user {user_id} from database...")
    # Simulate database query
    return {
        "id": user_id,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "orders": [101, 102, 103]
    }


def fetch_order_data(order_ids: List[int]) -> List[Dict[str, Any]]:
    """
    Fetches order data for given IDs.
    
    Args:
        order_ids: List of order IDs
    
    Returns:
        List of order dictionaries
    
    Real-world use case: Batch data fetching.
    """
    print(f"  → Fetching {len(order_ids)} orders from database...")
    # Simulate database query
    return [
        {"id": oid, "total": 99.99, "status": "completed"}
        for oid in order_ids
    ]


def calculate_user_metrics(user_data: Dict, orders: List[Dict]) -> Dict[str, Any]:
    """
    Calculates user analytics metrics.
    
    Args:
        user_data: User information
        orders: User's orders
    
    Returns:
        Analytics metrics dictionary
    
    Real-world use case: Analytics calculation.
    """
    print(f"  → Calculating metrics for user {user_data['id']}...")
    
    total_spent = sum(order["total"] for order in orders)
    order_count = len(orders)
    avg_order_value = total_spent / order_count if order_count > 0 else 0
    
    return {
        "total_orders": order_count,
        "total_spent": total_spent,
        "average_order_value": avg_order_value,
        "customer_tier": "VIP" if total_spent > 500 else "Standard"
    }


def format_report(user_data: Dict, metrics: Dict) -> str:
    """
    Formats analytics report for display.
    
    Args:
        user_data: User information
        metrics: Calculated metrics
    
    Returns:
        Formatted report string
    
    Real-world use case: Report generation.
    """
    print(f"  → Formatting report...")
    
    report = f"""
{'='*60}
USER ANALYTICS REPORT
{'='*60}
User: {user_data['name']} ({user_data['email']})
ID: {user_data['id']}

Metrics:
  - Total Orders: {metrics['total_orders']}
  - Total Spent: ${metrics['total_spent']:.2f}
  - Average Order: ${metrics['average_order_value']:.2f}
  - Customer Tier: {metrics['customer_tier']}
{'='*60}
"""
    return report


def generate_user_analytics_report(user_id: int) -> str:
    """
    Orchestrates the complete report generation workflow.
    
    Decomposition: Complex task broken into smaller, manageable steps.
    Each step is a separate function with single responsibility.
    
    Args:
        user_id: User identifier
    
    Returns:
        Formatted analytics report
    
    Real-world use case: Report generation pipeline, ETL orchestration.
    """
    print(f"\nGenerating analytics report for user {user_id}")
    print("-" * 60)
    
    # Step 1: Fetch user data
    user_data = fetch_user_data(user_id)
    
    # Step 2: Fetch related orders
    orders = fetch_order_data(user_data["orders"])
    
    # Step 3: Calculate metrics
    metrics = calculate_user_metrics(user_data, orders)
    
    # Step 4: Format report
    report = format_report(user_data, metrics)
    
    print(f"  ✓ Report generated successfully")
    return report


def extract_data_from_api(endpoint: str) -> Dict:
    """Step 1 of ETL: Extract data from API."""
    print(f"  [EXTRACT] Fetching data from {endpoint}...")
    return {"records": [{"id": 1, "value": 100}, {"id": 2, "value": 200}]}


def transform_data(raw_data: Dict) -> List[Dict]:
    """Step 2 of ETL: Transform/clean data."""
    print(f"  [TRANSFORM] Processing {len(raw_data['records'])} records...")
    
    transformed = []
    for record in raw_data["records"]:
        transformed.append({
            "id": record["id"],
            "value": record["value"],
            "processed_value": record["value"] * 1.1,  # Apply 10% markup
            "timestamp": datetime.now().isoformat()
        })
    
    return transformed


def load_data_to_warehouse(data: List[Dict]) -> bool:
    """Step 3 of ETL: Load data into warehouse."""
    print(f"  [LOAD] Writing {len(data)} records to data warehouse...")
    # Simulate database insert
    return True


def run_etl_pipeline(api_endpoint: str) -> bool:
    """
    Orchestrates ETL (Extract, Transform, Load) pipeline.
    
    Decomposition: Complex ETL process broken into 3 clear steps.
    
    Args:
        api_endpoint: Source API endpoint
    
    Returns:
        True if pipeline succeeded
    
    Real-world use case: Data engineering pipelines.
    """
    print(f"\nRunning ETL Pipeline")
    print("-" * 60)
    
    try:
        # Step 1: Extract
        raw_data = extract_data_from_api(api_endpoint)
        
        # Step 2: Transform
        transformed_data = transform_data(raw_data)
        
        # Step 3: Load
        success = load_data_to_warehouse(transformed_data)
        
        print(f"  ✓ ETL Pipeline completed successfully")
        return success
    
    except Exception as e:
        print(f"  ✗ ETL Pipeline failed: {e}")
        return False


def main() -> None:
    """Main function demonstrating function decomposition."""
    print("="*70)
    print("FUNCTION DECOMPOSITION & ABSTRACTION".center(70))
    print("="*70)
    
    print("\n[1] USER ANALYTICS REPORT GENERATION")
    print("=" * 70)
    
    report = generate_user_analytics_report(user_id=101)
    print(report)
    
    print("\n\n[2] ETL PIPELINE ORCHESTRATION")
    print("=" * 70)
    
    success = run_etl_pipeline("/api/sales")
    print(f"\nPipeline result: {'SUCCESS' if success else 'FAILED'}")
    
    print("\n\n" + "="*70)
    print("Benefits of Decomposition:")
    print("-" * 70)
    print("✓ Single Responsibility: Each function does ONE thing well")
    print("✓ Testability: Test each step independently")
    print("✓ Reusability: Steps can be reused in other workflows")
    print("✓ Readability: High-level view shows workflow clearly")
    print("✓ Maintainability: Easy to modify individual steps")
    print("✓ Debugging: Isolate issues to specific functions")
    print("="*70)


if __name__ == "__main__":
    main()