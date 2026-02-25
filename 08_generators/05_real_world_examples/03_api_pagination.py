"""
Topic: API Pagination via Generators.

Hides the complexity of making multiple paginated API requests 
behind a simple generator interface.
"""

def api_paginator(total_pages):
    for page in range(1, total_pages + 1):
        # Simulate network request
        print(f"  [API] Fetching results for page {page}...")
        results = [f"Item-{page}-{i}" for i in range(1, 4)] # 3 items/page
        yield from results

if __name__ == "__main__":
    all_results = api_paginator(total_pages=3)
    
    print("Consuming API Stream:")
    for item in all_results:
        print(f"    Got: {item}")
