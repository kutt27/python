"""
Merging User Data with zip().
"""

from typing import List, Dict

def merge_user_data(
    ids: List[int],
    usernames: List[str],
    emails: List[str]
) -> List[Dict[str, any]]:
    """
    Merges related user data from separate lists.
    
    Args:
        ids: User IDs
        usernames: Usernames
        emails: Email addresses
    
    Returns:
        List of user dictionaries
    
    Real-world use case: Combining data from multiple database queries.
    """
    users = []
    
    for user_id, username, email in zip(ids, usernames, emails):
        user = {
            "id": user_id,
            "username": username,
            "email": email
        }
        users.append(user)
    
    return users


def demonstrate_user_merge() -> None:
    """
    Demonstrates merging data from multiple sources.
    """
    user_ids = [101, 102, 103, 104]
    usernames = ["alice", "bob", "charlie", "diana"]
    user_emails = ["alice@example.com", "bob@example.com", 
                   "charlie@example.com", "diana@example.com"]
    
    merged_users = merge_user_data(user_ids, usernames, user_emails)
    
    print("\nMerged user data:")
    for user in merged_users:
        print(f"  ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")


if __name__ == "__main__":
    demonstrate_user_merge()
