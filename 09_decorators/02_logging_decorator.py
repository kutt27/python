"""
Python Decorators: Logging Patterns
====================================

Topic: Logging decorators, structured logging, audit trails

Real-World Applications:
- API request logging
- Audit trails for compliance
- Performance monitoring
- Error tracking
- User activity logging
"""

from functools import wraps
from datetime import datetime
from typing import Callable, Any
import json


def log_function_call(func: Callable) -> Callable:
    """
    Logs function calls with timestamp.
    
    Real-world use case: API endpoint logging, debugging.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] 🚀 Calling: {func.__name__}()")
        
        result = func(*args, **kwargs)
        
        print(f"[{timestamp}] ✅ Finished: {func.__name__}()")
        return result
    
    return wrapper


def log_with_arguments(func: Callable) -> Callable:
    """
    Logs function calls with full argument details.
    
    Real-world use case: API debugging, request tracing.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        timestamp = datetime.now().isoformat()
        
        log_entry = {
            "timestamp": timestamp,
            "function": func.__name__,
            "arguments": {"args": args, "kwargs": kwargs},
            "signature": signature
        }
        
        print(f"📝 CALL: {json.dumps(log_entry, indent=2)}")
        
        result = func(*args, **kwargs)
        
        result_log = {
            "timestamp": datetime.now().isoformat(),
            "function": func.__name__,
            "returned": str(result)[:100]  # Truncate long results
        }
        
        print(f"📝 RETURN: {json.dumps(result_log, indent=2)}")
        
        return result
    
    return wrapper


def audit_trail(action: str):
    """
    Decorator factory for audit logging.
    
    Args:
        action: Action description for audit log
    
    Real-world use case: Compliance, security audits.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Pre-execution audit
            audit_entry = {
                "timestamp": datetime.now().isoformat(),
                "action": action,
                "function": func.__name__,
                "user": kwargs.get("user_id", "unknown"),
                "details": {"args": str(args), "kwargs": str(kwargs)}
            }
            
            print(f"📋 AUDIT: {json.dumps(audit_entry)}")
            
            result = func(*args, **kwargs)
            
            # Post-execution audit
            success_entry = {
                "timestamp": datetime.now().isoformat(),
                "action": action,
                "status": "completed",
                "function": func.__name__
            }
            
            print(f"📋 AUDIT: {json.dumps(success_entry)}")
            
            return result
        
        return wrapper
    
    return decorator


def log_errors(func: Callable) -> Callable:
    """
    Logs errors with full context.
    
    Real-world use case: Error tracking, monitoring.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_log = {
                "timestamp": datetime.now().isoformat(),
                "function": func.__name__,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "arguments": {"args": args, "kwargs": kwargs}
            }
            
            print(f"❌ ERROR: {json.dumps(error_log, indent=2)}")
            raise
    
    return wrapper


def performance_logger(threshold_ms: float = 100):
    """
    Logs slow function executions.
    
    Args:
        threshold_ms: Threshold in milliseconds
    
    Real-world use case: Performance optimization, slow query detection.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            import time
            
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            
            elapsed_ms = (end - start) * 1000
            
            if elapsed_ms > threshold_ms:
                slow_log = {
                    "timestamp": datetime.now().isoformat(),
                    "function": func.__name__,
                    "elapsed_ms": round(elapsed_ms, 2),
                    "threshold_ms": threshold_ms,
                    "status": "SLOW"
                }
                
                print(f"⚠️  SLOW: {json.dumps(slow_log)}")
            
            return result
        
        return wrapper
    
    return decorator


# Example usage

@log_function_call
def process_order(order_id: str) -> dict:
    """Processes an order."""
    return {"order_id": order_id, "status": "processed"}


@log_with_arguments
def create_user(username: str, email: str, role: str = "user") -> dict:
    """Creates a new user."""
    return {
        "username": username,
        "email": email,
        "role": role,
        "created_at": datetime.now().isoformat()
    }


@audit_trail(action="DELETE_USER")
def delete_user_account(user_id: int, *, admin_id: int) -> bool:
    """Deletes user account (audited action)."""
    print(f"  Deleting user {user_id} by admin {admin_id}")
    return True


@log_errors
def risky_operation(value: int) -> int:
    """Operation that might fail."""
    if value < 0:
        raise ValueError("Value must be positive")
    return value * 2


@performance_logger(threshold_ms=50)
def database_query() -> list:
    """Simulates database query."""
    import time
    time.sleep(0.1)  # Simulate slow query
    return [1, 2, 3, 4, 5]


def main() -> None:
    """Main function demonstrating logging decorators."""
    print("="*70)
    print("LOGGING DECORATORS".center(70))
    print("="*70)
    
    print("\n[1] BASIC FUNCTION CALL LOGGING")
    print("-" * 70)
    
    order = process_order("ORD-12345")
    print(f"Result: {order}")
    
    print("\n\n[2] DETAILED ARGUMENT LOGGING")
    print("-" * 70)
    
    user = create_user("alice", "alice@example.com", role="admin")
    
    print("\n\n[3] AUDIT TRAIL LOGGING")
    print("-" * 70)
    
    deleted = delete_user_account(101, admin_id=999)
    print(f"Deletion successful: {deleted}")
    
    print("\n\n[4] ERROR LOGGING")
    print("-" * 70)
    
    try:
        result1 = risky_operation(10)
        print(f"✓ Success: {result1}")
        
        result2 = risky_operation(-5)
    except ValueError:
        print("✗ Operation failed (logged above)")
    
    print("\n\n[5] PERFORMANCE LOGGING")
    print("-" * 70)
    
    results = database_query()
    print(f"Query returned {len(results)} results")
    
    print("\n\n[6] STACKED LOGGING DECORATORS")
    print("-" * 70)
    
    @log_function_call
    @log_errors
    @performance_logger(threshold_ms=10)
    def complex_api_endpoint(request_id: str) -> dict:
        """API endpoint with multiple logging layers."""
        import time
        time.sleep(0.02)
        return {"request_id": request_id, "data": [1, 2, 3]}
    
    response = complex_api_endpoint("REQ-789")
    print(f"Response: {response}")
    
    print("\n" + "="*70)
    print("Logging Decorator Best Practices:")
    print("-" * 70)
    print("• Use structured logging (JSON) for log aggregation")
    print("• Include timestamps for all log entries")
    print("• Log both inputs and outputs for debugging")
    print("• Create audit trails for sensitive operations")
    print("• Track performance metrics automatically")
    print("• Separate concerns: error logging vs audit logging")
    print("\nCommon Logging Scenarios:")
    print("✓ API request/response logging")
    print("✓ Security audit trails")
    print("✓ Performance monitoring")
    print("✓ Error tracking and debugging")
    print("✓ Compliance requirements")
    print("="*70)


if __name__ == "__main__":
    main()