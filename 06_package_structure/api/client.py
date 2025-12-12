"""
API Client Package - HTTP Client Module
========================================

This module provides HTTP client functionality.

Real-World Application: RESTful API client, HTTP request handling
"""

from typing import Dict, Optional, Any
import json


class HTTPError(Exception):
    """Raised when HTTP request fails."""
    
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"HTTP {status_code}: {message}")


class HTTPClient:
    """
    Simple HTTP client for API requests.
    
    Real-world use case: API client implementation, requests wrapper.
    """
    
    def __init__(self, base_url: str, default_headers: Optional[Dict[str, str]] = None):
        """
        Initialize HTTP client.
        
        Args:
            base_url: Base URL for API
            default_headers: Default headers for all requests
        """
        self.base_url = base_url.rstrip("/")
        self.default_headers = default_headers or {}
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Sends GET request.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
        
        Returns:
            Response data
        
        Raises:
            HTTPError: If request fails
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # Simulate HTTP GET
        print(f"GET {url}")
        if params:
            print(f"  Params: {params}")
        
        # Simulated response
        return {
            "status": "success",
            "data": {"message": f"GET {endpoint} successful"}
        }
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Sends POST request.
        
        Args:
            endpoint: API endpoint
            data: Request body data
        
        Returns:
            Response data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # Simulate HTTP POST
        print(f"POST {url}")
        if data:
            print(f"  Data: {json.dumps(data, indent=2)}")
        
        # Simulated response
        return {
            "status": "success",
            "data": {"id": 12345, "created": True}
        }
    
    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Sends PUT request.
        
        Args:
            endpoint: API endpoint
            data: Request body data
        
        Returns:
            Response data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        print(f"PUT {url}")
        if data:
            print(f"  Data: {json.dumps(data, indent=2)}")
        
        return {"status": "success", "data": {"updated": True}}
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """
        Sends DELETE request.
        
        Args:
            endpoint: API endpoint
        
        Returns:
            Response data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        print(f"DELETE {url}")
        
        return {"status": "success", "data": {"deleted": True}}
