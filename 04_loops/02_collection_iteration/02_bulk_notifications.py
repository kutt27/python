"""
Bulk Notification sending.
"""

from typing import List, Tuple

def send_notifications(users: List[str], message: str) -> List[Tuple[str, bool]]:
    """
    Sends notifications to list of users.
    
    Args:
        users: List of usernames/emails
        message: Notification message
    
    Returns:
        List of (user, success) tuples
    
    Real-world use case: Bulk email sending, push notifications.
    """
    results = []
    
    print(f"\nSending notification: '{message}'")
    print("-" * 60)
    
    for user in users:
        # Simulate sending notification
        print(f"  → Sending to {user}")
        
        # Simulate success/failure
        success = len(user) > 0  # Simplified
        results.append((user, success))
    
    return results


def demonstrate_bulk_notifications() -> None:
    """
    Demonstrates sending notifications in bulk using iteration.
    
    Real-world use case: Communication systems, email dispatchers.
    """
    users = ["alice@example.com", "bob@example.com", "charlie@example.com"]
    results = send_notifications(users, "System maintenance tonight at 2 AM")
    
    successful = sum(1 for _, success in results if success)
    print(f"\nSent {successful}/{len(results)} notifications successfully")


if __name__ == "__main__":
    demonstrate_bulk_notifications()
