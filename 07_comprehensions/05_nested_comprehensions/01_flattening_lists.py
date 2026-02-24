"""
Topic: Flattening Nested Lists.

Nested comprehensions can be used to "flatten" a list of lists 
into a single flat list. 
Syntax: `[item for sublist in outer_list for item in sublist]`
"""

def demonstrate_flattening():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Flattening logic
    flat = [num for row in matrix for num in row]
    
    print(f"Matrix: {matrix}")
    print(f"Flat:   {flat}")

if __name__ == "__main__":
    demonstrate_flattening()
