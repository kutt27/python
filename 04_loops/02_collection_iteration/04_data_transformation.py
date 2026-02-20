"""
Data Transformation.
"""

from typing import List, Dict

def transform_user_data(raw_data: List[Dict]) -> List[Dict]:
    """
    Transforms raw user data for API response.
    
    Args:
        raw_data: Raw database records
    
    Returns:
        Transformed data for API
    
    Real-world use case: Data transformation, API serialization.
    """
    transformed = []
    
    for record in raw_data:
        # Transform each record
        transformed_record = {
            "id": record.get("user_id"),
            "name": record.get("full_name", "").title(),
            "email": record.get("email_address", "").lower(),
            "active": record.get("status") == "active"
        }
        transformed.append(transformed_record)
    
    return transformed


def demonstrate_data_transformation() -> None:
    """
    Demonstrates data transformation during collection iteration.
    
    Real-world use case: ETL, API response formatting.
    """
    raw_user_data = [
        {"user_id": 1, "full_name": "alice smith", "email_address": "ALICE@EXAMPLE.COM", "status": "active"},
        {"user_id": 2, "full_name": "bob jones", "email_address": "bob@EXAMPLE.com", "status": "inactive"},
    ]
    
    transformed_data = transform_user_data(raw_user_data)
    print("\nTransformed data:")
    for user in transformed_data:
        print(f"  {user}")


if __name__ == "__main__":
    demonstrate_data_transformation()
