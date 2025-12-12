"""
Python For Loops: List Processing with enumerate()
===================================================

Topic: enumerate() for index/value iteration

Real-World Applications:
- Position tracking in data processing
- Progress reporting in long operations
- Line number tracking in file parsing
- Indexed updates in databases
- Ranking and ordering systems
"""

from typing import List, Dict, Tuple


def process_orders_with_tracking(orders: List[str]) -> None:
    """
    Processes orders with position tracking.
    
    Args:
        orders: List of order IDs
    
    Real-world use case: Order processing with progress tracking.
    """
    total = len(orders)
    print(f"\nProcessing {total} orders")
    print("-" * 60)
    
    for index, order_id in enumerate(orders, start=1):
        progress = (index / total) * 100
        print(f"[{index}/{total}] ({progress:.0f}%) Processing order: {order_id}")


def parse_log_file_with_line_numbers(log_lines: List[str]) -> List[Tuple[int, str]]:
    """
    Parses log file and tracks line numbers for errors.
    
    Args:
        log_lines: List of log file lines
    
    Returns:
        List of (line_number, error_message) tuples
    
    Real-world use case: Log file analysis, error tracking.
    """
    errors = []
    
    print(f"\nParsing {len(log_lines)} log lines")
    print("-" * 60)
    
    for line_num, line in enumerate(log_lines, start=1):
        if "ERROR" in line:
            errors.append((line_num, line.strip()))
            print(f"  Line {line_num}: Found error - {line.strip()}")
    
    return errors


def rank_search_results(results: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Adds ranking to search results.
    
    Args:
        results: List of search result dictionaries
    
    Returns:
        Results with ranking added
    
    Real-world use case: Search engines, recommendation systems.
    """
    ranked_results = []
    
    for rank, result in enumerate(results, start=1):
        result_with_rank = result.copy()
        result_with_rank["rank"] = rank
        ranked_results.append(result_with_rank)
    
    return ranked_results


def batch_update_with_progress(items: List[Dict], batch_size: int = 5) -> None:
    """
    Performs batch updates with progress reporting.
    
    Args:
        items: Items to update
        batch_size: Size of each batch
    
    Real-world use case: Database batch updates, bulk operations.
    """
    total = len(items)
    print(f"\nBatch updating {total} items (batch size: {batch_size})")
    print("-" * 60)
    
    for index, item in enumerate(items):
        # Determine batch number and position
        batch_num = (index // batch_size) + 1
        position_in_batch = (index % batch_size) + 1
        
        print(f"Batch {batch_num}, Item {position_in_batch}/{batch_size}: Updating {item.get('id')}")
        
        # Commit batch when complete
        if (index + 1) % batch_size == 0 or (index + 1) == total:
            items_in_batch = min(batch_size, total - (batch_num - 1) * batch_size)
            print(f"  → Committing batch {batch_num} ({items_in_batch} items)")


def find_duplicates_with_positions(items: List[str]) -> Dict[str, List[int]]:
    """
    Finds duplicate items and their positions.
    
    Args:
        items: List of items to check
    
    Returns:
        Dictionary mapping items to their position indices
    
    Real-world use case: Data validation, duplicate detection.
    """
    positions: Dict[str, List[int]] = {}
    
    for index, item in enumerate(items):
        if item not in positions:
            positions[item] = []
        positions[item].append(index)
    
    # Filter to only duplicates
    duplicates = {k: v for k, v in positions.items() if len(v) > 1}
    
    return duplicates


def create_indexed_backup(files: List[str], backup_dir: str = "/backups") -> None:
    """
    Creates indexed backup files.
    
    Args:
        files: List of files to backup
        backup_dir: Backup directory path
    
    Real-world use case: Backup systems, file versioning.
    """
    print(f"\nCreating indexed backups in {backup_dir}")
    print("-" * 60)
    
    for index, filename in enumerate(files):
        # Create versioned backup name
        backup_name = f"{filename}.backup.{index + 1}"
        backup_path = f"{backup_dir}/{backup_name}"
        
        print(f"  [{index + 1}] {filename} → {backup_path}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("FOR LOOPS: enumerate() FOR INDEX TRACKING".center(70))
    print("="*70)
    
    print("\n[1] ORDER PROCESSING WITH PROGRESS")
    print("-" * 70)
    
    orders = ["ORD-101", "ORD-102", "ORD-103", "ORD-104", "ORD-105"]
    process_orders_with_tracking(orders)
    
    print("\n\n[2] LOG FILE PARSING WITH LINE NUMBERS")
    print("-" * 70)
    
    log_lines = [
        "2024-12-05 10:00:00 INFO Server started",
        "2024-12-05 10:01:23 ERROR Database connection failed",
        "2024-12-05 10:02:15 INFO Request processed",
        "2024-12-05 10:03:45 ERROR Timeout on external API",
        "2024-12-05 10:04:00 INFO Shutting down",
    ]
    
    errors = parse_log_file_with_line_numbers(log_lines)
    print(f"\nFound {len(errors)} errors in log file")
    
    print("\n\n[3] SEARCH RESULT RANKING")
    print("-" * 70)
    
    search_results = [
        {"title": "Python Tutorial", "score": 0.95},
        {"title": "Python Documentation", "score": 0.89},
        {"title": "Learn Python", "score": 0.82},
    ]
    
    ranked = rank_search_results(search_results)
    print("\nRanked search results:")
    for result in ranked:
        print(f"  #{result['rank']}: {result['title']} (Score: {result['score']})")
    
    print("\n\n[4] BATCH UPDATES WITH PROGRESS")
    print("-" * 70)
    
    items_to_update = [
        {"id": f"ITEM-{i}"} for i in range(1, 13)
    ]
    
    batch_update_with_progress(items_to_update, batch_size=5)
    
    print("\n\n[5] DUPLICATE DETECTION")
    print("-" * 70)
    
    data = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
    duplicates = find_duplicates_with_positions(data)
    
    print(f"\nChecking {len(data)} items for duplicates")
    if duplicates:
        for item, positions in duplicates.items():
            print(f"  '{item}' appears {len(positions)} times at positions: {positions}")
    else:
        print("  No duplicates found")
    
    print("\n\n[6] INDEXED BACKUP CREATION")
    print("-" * 70)
    
    files_to_backup = ["config.json", "database.db", "logs.txt"]
    create_indexed_backup(files_to_backup)
    
    print("\n" + "="*70)
    print(" Key Takeaways:")
    print("1. enumerate(iterable) returns (index, value) pairs")
    print("2. enumerate(iterable, start=N) starts counting from N")
    print("3. Useful for tracking position while iterating")
    print("4. Commonly used for progress reporting")
    print("5. Alternative to manual counter variables")
    print("="*70)


if __name__ == "__main__":
    main()