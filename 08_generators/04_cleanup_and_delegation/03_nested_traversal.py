"""
Topic: Recursive Tree Traversal with `yield from`.

`yield from` is perfect for recursively traversing nested 
structures like file systems or tree data.
"""

def traverse_tree(node):
    # Yield current node's value
    yield node["value"]
    
    # Recursively yield from children
    for child in node.get("children", []):
        yield from traverse_tree(child)

if __name__ == "__main__":
    tree = {
        "value": "root",
        "children": [
            {"value": "child1", "children": [{"value": "grandchild1"}]},
            {"value": "child2"}
        ]
    }
    
    print("Tree Nodes:")
    for node in traverse_tree(tree):
        print(f"  - {node}")
