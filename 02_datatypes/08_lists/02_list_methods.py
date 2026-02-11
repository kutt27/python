"""
Demonstrates essential list methods: append, insert, extend, remove, and pop.
"""

def demonstrate_list_methods() -> None:
    stages = ["build", "test"]
    print(f"Original: {stages}")
    
    stages.append("deploy")
    print(f"Append: {stages}")
    
    stages.insert(1, "lint")
    print(f"Insert at [1]: {stages}")
    
    stages.extend(["monitor", "notify"])
    print(f"Extend: {stages}")
    
    stages.remove("lint")
    print(f"Remove 'lint': {stages}")
    
    print(f"Pop last: {stages.pop()}")
    print(f"Final: {stages}")

if __name__ == "__main__":
    demonstrate_list_methods()
