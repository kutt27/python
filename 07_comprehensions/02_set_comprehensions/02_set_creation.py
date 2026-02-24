"""
Topic: Extracting Unique Sets of Data.

Set comprehensions are excellent for finding all unique 
categories, tags, or features across a collection of records.
"""

def demonstrate_tag_extraction():
    blog_posts = [
        {"title": "Intro to Python", "tags": ["python", "basics"]},
        {"title": "Web Scraper", "tags": ["python", "web", "data"]},
        {"title": "React Guide", "tags": ["javascript", "web"]},
    ]
    
    # Extract all unique tags across all posts
    all_tags = {tag for post in blog_posts for tag in post["tags"]}
    
    print(f"Total Unique Tags: {sorted(all_tags)}")

if __name__ == "__main__":
    demonstrate_tag_extraction()
