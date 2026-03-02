"""
Topic: Class vs Instance Attributes.

Class attributes are shared by ALL instances. 
Instance attributes are unique to EACH instance.
"""

class Server:
    # Class attribute - shared by all servers
    default_timeout = 30
    
    def __init__(self, name: str):
        # Instance attribute - specific to this server
        self.name = name

if __name__ == "__main__":
    web = Server("Web-01")
    db = Server("DB-01")
    
    print(f"{web.name} timeout: {web.default_timeout}")
    print(f"{db.name} timeout: {db.default_timeout}")
    
    # Changing the class attribute affects all instances
    Server.default_timeout = 60
    print("\nAfter updating class attribute:")
    print(f"Web: {web.default_timeout}")
    print(f"DB:  {db.default_timeout}")
