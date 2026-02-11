"""
Demonstrates dictionary-based caching and merging user preferences with defaults.
"""

from typing import Dict, Any

def get_user(uid: int, cache: Dict[int, Any]) -> Any:
    if uid in cache:
        print(f"HIT (UID {uid})")
        return cache[uid]
    
    print(f"MISS (UID {uid}) - Fetching...")
    user = {"id": uid, "name": f"User{uid}"}
    cache[uid] = user
    return user

def merge_prefs(defaults: Dict[str, Any], user_prefs: Dict[str, Any]) -> Dict[str, Any]:
    final = defaults.copy()
    final.update(user_prefs)
    return final

if __name__ == "__main__":
    # Caching
    cache = {}
    get_user(1, cache)
    get_user(1, cache)
    
    # Merging
    defaults = {"theme": "light", "notifs": True}
    user = {"theme": "dark"}
    print(f"\nFinal Config: {merge_prefs(defaults, user)}")
