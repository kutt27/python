"""
API Response Processing.
"""

from typing import Dict, Any

def process_api_response(response: Dict[str, Any]) -> None:
    """
    Processes API response by iterating through fields.
    
    Args:
        response: API response dictionary
    
    Real-world use case: API integration, response validation.
    """
    print("\nProcessing API Response:")
    print("-" * 60)
    
    # Iterate over items (key-value pairs)
    for field, value in response.items():
        print(f"  {field}: {value}")


def demonstrate_api_processing() -> None:
    """
    Demonstrates API response processing.
    """
    api_response = {
        "status": "success",
        "code": 200,
        "data": {"users": 42},
        "timestamp": "2024-12-05T10:00:00Z"
    }
    
    process_api_response(api_response)


if __name__ == "__main__":
    demonstrate_api_processing()
