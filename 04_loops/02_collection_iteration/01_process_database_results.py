"""
Database Result Processing with loops.
"""

from typing import List, Dict

def process_database_results(records: List[Dict]) -> None:
    """
    Processes database query results.
    
    Args:
        records: List of database records
    
    Real-world use case: ORM result processing, data validation.
    """
    print(f"\nProcessing {len(records)} database records")
    print("-" * 60)
    
    for record in records:
        user_id = record.get("id")
        username = record.get("username")
        status = record.get("status", "unknown")
        
        # Process each record
        print(f"User {user_id}: {username} (Status: {status})")


def demonstrate_database_processing() -> None:
    """
    Demonstrates iteration over database query results.
    
    Real-world use case: Processing records from an ORM or database.
    """
    db_records = [
        {"id": 1, "username": "alice", "status": "active"},
        {"id": 2, "username": "bob", "status": "inactive"},
        {"id": 3, "username": "charlie", "status": "active"},
    ]
    process_database_results(db_records)


if __name__ == "__main__":
    demonstrate_database_processing()
