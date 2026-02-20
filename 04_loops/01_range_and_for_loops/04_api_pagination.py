"""
API Pagination logic.
"""

from typing import List

def paginate_results(total_items: int, page_size: int = 20) -> List[tuple]:
    """
    Generates pagination ranges for API responses.
    
    Args:
        total_items: Total number of items
        page_size: Items per page
    
    Returns:
        List of (page_number, start_index, end_index) tuples
    
    Real-world use case: API pagination, database query chunking.
    """
    pages = []
    total_pages = (total_items + page_size - 1) // page_size
    
    for page in range(1, total_pages + 1):
        start = (page - 1) * page_size
        end = min(start + page_size, total_items)
        pages.append((page, start, end))
    
    return pages


def demonstrate_api_pagination() -> None:
    """
    Demonstrates pagination logic using range() and calculations.
    
    Real-world use case: API endpoints, search results.
    """
    total_records = 87
    page_size = 20
    
    pages = paginate_results(total_records, page_size)
    print(f"\nTotal records: {total_records}, Page size: {page_size}")
    print(f"Total pages: {len(pages)}\n")
    
    for page_num, start, end in pages:
        items_count = end - start
        print(f"Page {page_num}: Records {start}-{end} ({items_count} items)")


if __name__ == "__main__":
    demonstrate_api_pagination()
