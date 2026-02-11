"""
Demonstrates pagination calculation using integer arithmetic.
"""

from typing import Tuple

def calculate_pagination(total_items: int, page_size: int) -> Tuple[int, int]:
    # Ceiling division formula: (total + size - 1) // size
    total_pages = (total_items + page_size - 1) // page_size
    items_on_last_page = total_items % page_size or page_size
    return total_pages, items_on_last_page

if __name__ == "__main__":
    total_items = 1000
    page_size = 25
    pages, last_page_items = calculate_pagination(total_items, page_size)
    print(f"Total items: {total_items}")
    print(f"Page size: {page_size}")
    print(f"Result: {pages} pages, {last_page_items} items on last page")
