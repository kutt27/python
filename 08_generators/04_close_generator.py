"""
Python Generators: close() and yield from
==========================================

Topic: Generator cleanup, delegation, exception handling

Real-World Applications:
- Resource cleanup (files, connections)
- Generator composition
- Delegating to sub-generators
- Graceful shutdown
- Generator hierarchies
"""

from typing import Generator, List


def managed_file_reader(filename: str) -> Generator[str, None, None]:
    """
    Reads file with proper cleanup.
    
    Args:
        filename: File to read
    
    Yields:
        File lines
    
    Real-world use case: File processing with guaranteed cleanup.
    """
    print(f"Opening file: {filename}")
    
    # Simulated file content
    lines = [
        "Line 1: Application started",
        "Line 2: Processing request",
        "Line 3: Request completed",
    ]
    
    try:
        for line in lines:
            yield line
    finally:
        # Cleanup code - runs even if generator.close() is called
        print(f"Closing file: {filename}")


def database_connection_handler(query: str) -> Generator[dict, None, None]:
    """
    Handles database connection with cleanup.
    
    Args:
        query: SQL query
    
    Yields:
        Query results
    
    Real-world use case: Database operations with connection cleanup.
    """
    print(f"Connecting to database...")
    
    # Simulated query results
    results = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]
    
    try:
        print(f"Executing query: {query}")
        for row in results:
            yield row
    finally:
        # Always runs, even if close() is called
        print("Closing database connection")


def local_data_source() -> Generator[str, None, None]:
    """Yields local data items."""
    print("  Loading local data...")
    yield "Local item 1"
    yield "Local item 2"
    yield "Local item 3"


def remote_data_source() -> Generator[str, None, None]:
    """Yields remote data items."""
    print("  Fetching remote data...")
    yield "Remote item 1"
    yield "Remote item 2"


def aggregated_data() -> Generator[str, None, None]:
    """
    Aggregates data from multiple sources using yield from.
    
    yield from delegates to sub-generators.
    
    Yields:
        Items from all sources
    
    Real-world use case: Combining multiple data sources.
    """
    print("Starting data aggregation")
    
    # Delegate to local source
    yield from local_data_source()
    
    # Delegate to remote source
    yield from remote_data_source()
    
    print("Data aggregation complete")


def fetch_api_pages(base_url: str, total_pages: int) -> Generator[List[dict], None, None]:
    """
    Fetches multiple API pages.
    
    Args:
        base_url: Base API URL
        total_pages: Number of pages to fetch
    
    Yields:
        Page data
    """
    for page in range(1, total_pages + 1):
        print(f"  Fetching page {page}...")
        # Simulated API response
        yield [{"page": page, "item": i} for i in range(1, 4)]


def fetch_all_api_data(base_url: str) -> Generator[dict, None, None]:
    """
    Fetches and flattens all API data using yield from.
    
    Args:
        base_url: Base API URL
    
    Yields:
        Individual items from all pages
    
    Real-world use case: API pagination, flattening nested data.
    """
    print(f"Fetching all data from {base_url}")
    
    # Get pages
    pages_gen = fetch_api_pages(base_url, total_pages=3)
    
    # Flatten pages into items using yield from
    for page_data in pages_gen:
        yield from page_data
    
    print("All data fetched")


def recursive_tree_traversal(tree: dict) -> Generator[str, None, None]:
    """
    Recursively traverses tree using yield from.
    
    Args:
        tree: Tree structure
    
    Yields:
        Node values
    
    Real-world use case: File system traversal, nested data processing.
    """
    # Yield current node value
    yield tree["value"]
    
    # Recursively yield from children
    for child in tree.get("children", []):
        yield from recursive_tree_traversal(child)


def main() -> None:
    """Main function demonstrating close() and yield from."""
    print("="*70)
    print("GENERATOR close() AND yield from".center(70))
    print("="*70)
    
    print("\n[1] GENERATOR CLEANUP WITH close()")
    print("-" * 70)
    
    file_gen = managed_file_reader("data.txt")
    
    # Read first 2 lines
    print(next(file_gen))
    print(next(file_gen))
    
    # Close generator (triggers finally block)
    print("\nCalling close()...")
    file_gen.close()
    print("Generator closed")
    
    print("\n\n[2] DATABASE CONNECTION CLEANUP")
    print("-" * 70)
    
    db_gen = database_connection_handler("SELECT * FROM users")
    
    # Fetch first result
    print(f"First result: {next(db_gen)}")
    
    # Stop early and cleanup
    print("\nClosing connection early...")
    db_gen.close()
    
    print("\n\n[3] DATA AGGREGATION WITH yield from")
    print("-" * 70)
    
    agg_gen = aggregated_data()
    
    print("\nAggregated items:")
    for item in agg_gen:
        print(f"  {item}")
    
    print("\n\n[4] API PAGINATION WITH yield from")
    print("-" * 70)
    
    api_gen = fetch_all_api_data("https://api.example.com/data")
    
    print("\nFetched items:")
    all_items = list(api_gen)
    print(f"  Total items: {len(all_items)}")
    print(f"  First 3 items: {all_items[:3]}")
    
    print("\n\n[5] RECURSIVE TREE TRAVERSAL")
    print("-" * 70)
    
    # Tree structure
    file see_tree = {
        "value": "root",
        "children": [
            {
                "value": "child1",
                "children": [
                    {"value": "grandchild1"},
                    {"value": "grandchild2"},
                ]
            },
            {
                "value": "child2",
                "children": [
                    {"value": "grandchild3"},
                ]
            },
        ]
    }
    
    print("Tree traversal (depth-first):")
    for node in recursive_tree_traversal(tree):
        print(f"  {node}")
    
    print("\n\n[6] EXCEPTION HANDLING IN GENERATORS")
    print("-" * 70)
    
    def generator_with_error():
        """Generator that handles exceptions."""
        try:
            print("  Starting generator...")
            yield 1
            yield 2
            yield 3
        except GeneratorExit:
            print("  Generator is being closed")
        finally:
            print("  Cleanup code executed")
    
    gen = generator_with_error()
    print(next(gen))
    print(next(gen))
    
    print("\nClosing generator:")
    gen.close()
    
    print("\n\n[7] COMPARISON: Manual vs yield from")
    print("-" * 70)
    
    def manual_delegation():
        """Manual iteration over sub-generator."""
        sub_gen = local_data_source()
        for item in sub_gen:
            yield item
    
    def yield_from_delegation():
        """Using yield from for delegation."""
        yield from local_data_source()
    
    print("Manual delegation:")
    for item in manual_delegation():
        print(f"  {item}")
    
    print("\nyield from delegation (simpler):")
    for item in yield_from_delegation():
        print(f"  {item}")
    
    print("\n" + "="*70)
    print("Generator Cleanup & Delegation:")
    print("-" * 70)
    print("close() Method:")
    print("• Raises GeneratorExit exception at yield point")
    print("• Triggers finally blocks for cleanup")
    print("• Use for resource management (files, connections)")
    print("\nyield from Statement:")
    print("• Delegates to sub-generator")
    print("• Transparently forwards all values")
    print("• Simplifies generator composition")
    print("• Better than manual for...yield loop")
    print("\nCommon Patterns:")
    print("try:")
    print("    # generator code")
    print("    yield value")
    print("finally:")
    print("    # cleanup (runs even if close() called)")
    print("\nUse Cases:")
    print("✓ File/connection cleanup")
    print("✓ Composing multiple generators")
    print("✓ Flattening nested iterables")
    print("✓ Recursive tree traversal")
    print("✓ Graceful shutdown")
    print("="*70)


if __name__ == "__main__":
    main()