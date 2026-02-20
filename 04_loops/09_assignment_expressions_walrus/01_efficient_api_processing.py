"""
Efficient API Response Processing with Walrus.
"""

from typing import List, Dict

def process_api_responses_efficient(responses: List[Dict]) -> List[Dict]:
    """
    Processes API responses using walrus operator for efficiency.
    
    Args:
        responses: List of API response dictionaries
    
    Returns:
        List of processed responses
    
    Real-world use case: API integration, response validation.
    """
    processed = []
    
    print("\nProcessing API responses with walrus operator")
    print("-" * 60)
    
    for response in responses:
        # Walrus operator: assign and use in same expression
        if (status := response.get('status')) == 'success':
            print(f"  ✓ Response {response.get('id')}: {status}")
            processed.append(response)
        else:
            print(f"  ✗ Response {response.get('id')}: {status}")
    
    return processed


def demonstrate_efficient_processing() -> None:
    """
    Demonstrates efficient processing with walrus operator.
    """
    api_responses = [
        {"id": 1, "status": "success", "data": {}},
        {"id": 2, "status": "error", "data": None},
        {"id": 3, "status": "success", "data": {}},
    ]
    
    valid = process_api_responses_efficient(api_responses)
    print(f"\nProcessed {len(valid)}/{len(api_responses)} successful responses")


if __name__ == "__main__":
    demonstrate_efficient_processing()
