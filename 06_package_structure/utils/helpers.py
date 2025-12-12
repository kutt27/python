"""
Package Structure - Utilities Module
=====================================

This module provides utility functions used across the package.

Real-World Application: Common utilities, helper functions
"""

from typing import Dict, Any, List
import re


def validate_email(email: str) -> bool:
    """
    Validates email format.
    
    Args:
        email: Email address to validate
    
    Returns:
        True if valid format
    
    Real-world use case: Input validation.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def sanitize_input(text: str) -> str:
    """
    Sanitizes user input by removing dangerous characters.
    
    Args:
        text: Input text
    
    Returns:
        Sanitized text
    
    Real-world use case: Security, XSS prevention.
    """
    # Remove <script> tags and other dangerous patterns
    dangerous_patterns = [
        r'<script[^>]*>.*?</script>',
        r'javascript:',
        r'on\w+\s*=',
    ]
    
    sanitized = text
    for pattern in dangerous_patterns:
        sanitized = re.sub(pattern, '', sanitized, flags=re.IGNORECASE)
    
    return sanitized.strip()


def format_response(data: Any, status: str = "success", error: str = None) -> Dict:
    """
    Formats API response in consistent structure.
    
    Args:
        data: Response data
        status: Response status
        error: Error message if any
    
    Returns:
        Formatted response dictionary
    
    Real-world use case: API response formatting.
    """
    return {
        "status": status,
        "data": data if status == "success" else None,
        "error": error if status == "error" else None
    }


def paginate_results(items: List, page: int = 1, page_size: int = 20) -> Dict:
    """
    Paginates list of items.
    
    Args:
        items: List of items to paginate
        page: Page number (1-indexed)
        page_size: Items per page
    
    Returns:
        Dictionary with paginated results and metadata
    
    Real-world use case: API pagination, large datasets.
    """
    total_items = len(items)
    total_pages = (total_items + page_size - 1) // page_size
    
    # Calculate slice indices
    start = (page - 1) * page_size
    end = start + page_size
    
    return {
        "items": items[start:end],
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_prev": page > 1
        }
    }


def retry_on_failure(func, max_retries: int = 3):
    """
    Decorator that retries function on failure.
    
    Args:
        func: Function to wrap
        max_retries: Maximum retry attempts
    
    Returns:
        Wrapped function
    
    Real-world use case: Network resilience, error handling.
    """
    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
    
    return wrapper
