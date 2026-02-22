"""
Topic: Tree Traversal Recursion.

Recursion is naturally suited for hierarchical data structures like 
folders or JSON objects.
"""

def calculate_folder_size(folder: dict) -> int:
    """Sum the sizes of this folder and all its subfolders."""
    size = folder.get("size", 0)
    
    # Recursive call for each subfolder
    for sub in folder.get("subfolders", []):
        size += calculate_folder_size(sub)
    
    return size

if __name__ == "__main__":
    fs = {
        "name": "root",
        "size": 10,
        "subfolders": [
            {"name": "images", "size": 100},
            {"name": "docs", "size": 50, "subfolders": [
                {"name": "pdf", "size": 200}
            ]}
        ]
    }
    
    print(f"Total size: {calculate_folder_size(fs)} KB")
