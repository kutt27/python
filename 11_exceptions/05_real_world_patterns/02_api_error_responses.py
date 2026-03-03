"""
Topic: API Error Formatting.

A common pattern is to catch various internal exceptions 
and "translate" them into a standardized format (like JSON) 
for an API response.
"""

import json
from datetime import datetime

class APIError(Exception):
    def __init__(self, message, status_code=500):
        self.message = message
        self.status_code = status_code
        self.timestamp = datetime.now().isoformat()

def mock_api_handler(request_data):
    try:
        if not request_data:
            raise APIError("Empty request body", 400)
        # Process logic here...
        return {"status": "success", "data": "processed"}
    except APIError as e:
        # Return a structured error response
        return {
            "error": True,
            "message": e.message,
            "code": e.status_code,
            "at": e.timestamp
        }

if __name__ == "__main__":
    print(f"Valid result: {mock_api_handler('data')}")
    print(f"Error result: {json.dumps(mock_api_handler(''), indent=2)}")
