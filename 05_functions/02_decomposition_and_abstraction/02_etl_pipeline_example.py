"""
Topic: ETL Pipeline Abstraction.

Demonstrates decomposing a data engineering process into 
Extract, Transform, and Load phases.
"""

from typing import Dict, List
from datetime import datetime

def extract_data() -> Dict:
    """Step 1: Extract data from source."""
    print("  [EXTRACT] Fetching raw records...")
    return {"records": [{"id": 1, "value": 100}, {"id": 2, "value": 200}]}

def transform_data(raw_data: Dict) -> List[Dict]:
    """Step 2: Clean and enrich data."""
    print(f"  [TRANSFORM] Processing {len(raw_data['records'])} records...")
    return [{**r, "processed_at": datetime.now().isoformat()} for r in raw_data["records"]]

def load_data(data: List[Dict]) -> bool:
    """Step 3: Load data to destination."""
    print(f"  [LOAD] Storing {len(data)} records in warehouse...")
    return True

def run_pipeline():
    """Main orchestration function."""
    raw = extract_data()
    clean = transform_data(raw)
    success = load_data(clean)
    print(f"Pipeline status: {'Success' if success else 'Failed'}")

if __name__ == "__main__":
    run_pipeline()
