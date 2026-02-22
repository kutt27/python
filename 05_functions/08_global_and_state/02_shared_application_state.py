"""
Topic: Shared Application State & Connection Pools.

Global variables are often used for shared resources like 
connection pools or caches that need to be accessed from 
anywhere in the application.
"""

# Global shared state
CONNECTION_POOL = {
    "max": 5,
    "active": 0
}

def get_connection():
    global CONNECTION_POOL
    if CONNECTION_POOL["active"] < CONNECTION_POOL["max"]:
        CONNECTION_POOL["active"] += 1
        print(f"Connection acquired. Active: {CONNECTION_POOL['active']}")
        return True
    print("Error: Connection pool exhausted")
    return False

def release_connection():
    global CONNECTION_POOL
    if CONNECTION_POOL["active"] > 0:
        CONNECTION_POOL["active"] -= 1
        print(f"Connection released. Active: {CONNECTION_POOL['active']}")

if __name__ == "__main__":
    for _ in range(3): get_connection()
    release_connection()
    get_connection()
