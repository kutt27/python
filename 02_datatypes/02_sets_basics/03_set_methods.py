"""
Demonstrates practical set methods like add(), update(), discard(), and membership testing.
"""

from typing import Set

def demonstrate_set_methods() -> None:
    active_sessions: Set[str] = set()
    
    # User logs in
    active_sessions.add("user_123")
    active_sessions.add("user_456")
    print(f"After logins: {active_sessions}")
    
    # Batch login
    new_logins = {"user_789", "user_101", "user_123"}
    active_sessions.update(new_logins)
    print(f"After batch login (duplicates ignored): {active_sessions}")
    
    # User logs out
    active_sessions.discard("user_456")
    print(f"After logout: {active_sessions}")
    
    # Membership testing (O(1))
    user_id = "user_789"
    print(f"Is {user_id} logged in? {user_id in active_sessions}")

if __name__ == "__main__":
    demonstrate_set_methods()
