"""
Demonstrates modifying sets with add(), update(), discard(), and clear().
"""

def demonstrate_modifications() -> None:
    tags = {"python", "programming"}
    print(f"Initial: {tags}")
    
    tags.add("tutorial")
    print(f"After add: {tags}")
    
    tags.update({"backend", "webdev"})
    print(f"After update: {tags}")
    
    tags.discard("webdev")
    print(f"After discard: {tags}")
    
    tags.clear()
    print(f"After clear: {tags}")

if __name__ == "__main__":
    demonstrate_modifications()
