"""
Paginated API Processing with break.
"""

def process_paginated_api(max_pages: int = 10) -> int:
    """
    Processes paginated API results, stops when no more data.
    
    Args:
        max_pages: Maximum pages to fetch
    
    Returns:
        Total items processed
    
    Real-world use case: API pagination handling.
    """
    total_items = 0
    page = 1
    
    print(f"\nFetching paginated API data (max {max_pages} pages)")
    print("-" * 60)
    
    while page <= max_pages:
        # Simulate API call
        items_in_page = 20 if page < 5 else 0  # No more data after page 4
        
        if items_in_page == 0:
            print(f"  Page {page}: No more data - stopping")
            break  # No more pages to fetch
        
        print(f"  Page {page}: Fetched {items_in_page} items")
        total_items += items_in_page
        page += 1
    
    return total_items


def demonstrate_pagination_break() -> None:
    """
    Demonstrates breaking pagination loop when no more data.
    """
    total = process_paginated_api(max_pages=10)
    print(f"\nTotal items fetched: {total}")


if __name__ == "__main__":
    demonstrate_pagination_break()
