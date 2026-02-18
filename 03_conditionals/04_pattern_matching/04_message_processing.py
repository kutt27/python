"""
Message Processing logic.
"""

from typing import Dict, Any

def process_message(message: Dict[str, Any]) -> str:
    """
    Processes different message types using pattern matching.
    
    Args:
        message: Message dictionary with type and data
    
    Returns:
        Processing result
    
    Real-world use case: Message queue processing, event handling.
    """
    match message:
        # User registration event
        case {"type": "user.registered", "email": email, "user_id": uid}:
            return f"📧 Send welcome email to {email} (User: {uid})"
        
        # Order placed event
        case {"type": "order.placed", "order_id": oid, "amount": amount}:
            return f"💳 Process payment for order {oid}: ${amount}"
        
        # Payment successful
        case {"type": "payment.success", "transaction_id": tid}:
            return f"✅ Payment confirmed: {tid}"
        
        # Error event
        case {"type": "error", "service": service, "message": msg}:
            return f"🚨 Alert: {service} error - {msg}"
        
        # Health check
        case {"type": "health_check"}:
            return "✓ Service responding"
        
        case _:
            return f"⚠ Unknown message type: {message.get('type', 'none')}"


def demonstrate_message_processing() -> None:
    """
    Demonstrates dictionary pattern matching for event handling.
    
    Real-world use case: Message queues, microservices.
    """
    messages = [
        {"type": "user.registered", "email": "alice@example.com", "user_id": 101},
        {"type": "order.placed", "order_id": "ORD-123", "amount": 99.99},
        {"type": "payment.success", "transaction_id": "TXN-456"},
        {"type": "error", "service": "payment-api", "message": "Connection timeout"},
        {"type": "health_check"},
        {"type": "unknown.event"},
    ]
    
    for msg in messages:
        result = process_message(msg)
        print(f"  {result}")


if __name__ == "__main__":
    demonstrate_message_processing()
