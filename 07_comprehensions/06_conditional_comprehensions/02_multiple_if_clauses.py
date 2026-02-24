"""
Topic: Multiple Filtering Clauses.

You can chain multiple `if` conditions at the end of a 
comprehension. Elements must satisfy ALL conditions to be included.
"""

def demonstrate_multi_if():
    nums = range(100)
    
    # Numbers that are divisible by 2 AND 5 AND greater than 50
    matches = [
        x for x in nums 
        if x > 50 
        if x % 2 == 0 
        if x % 5 == 0
    ]
    
    print(f"Matches: {matches}")

if __name__ == "__main__":
    demonstrate_multi_if()
