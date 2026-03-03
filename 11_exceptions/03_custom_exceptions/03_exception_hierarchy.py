"""
Topic: Exception Hierarchies.

By creating a base exception for your application, you allow 
callers to catch all your custom errors with a single block, 
or target specific ones.
"""

class AppError(Exception):
    """Base exception for the whole app."""
    pass

class DatabaseError(AppError):
    """Errors related to DB operations."""
    pass

class NetworkError(AppError):
    """Errors related to network calls."""
    pass

if __name__ == "__main__":
    try:
        raise DatabaseError("Lost connection to SQL")
    except AppError as e:
        print(f"Caught a general application error: {type(e).__name__} - {e}")
