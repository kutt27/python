"""
Database Synchronization.
"""

from typing import List

def sync_database_records(
    local_ids: List[int],
    remote_ids: List[int],
    local_hashes: List[str],
    remote_hashes: List[str]
) -> List[int]:
    """
    Identifies records that need syncing between databases.
    
    Args:
        local_ids: Local database IDs
        remote_ids: Remote database IDs
        local_hashes: Local record hashes
        remote_hashes: Remote record hashes
    
    Returns:
        List of IDs that need syncing
    
    Real-world use case: Database synchronization, data replication.
    """
    needs_sync = []
    
    print("\nDatabase Synchronization Check")
    print("-" * 60)
    
    for local_id, remote_id, local_hash, remote_hash in zip(
        local_ids, remote_ids, local_hashes, remote_hashes
    ):
        if local_hash != remote_hash:
            needs_sync.append(local_id)
            print(f"  Record {local_id}: OUT OF SYNC")
        else:
            print(f"  Record {local_id}: ✓ Synced")
    
    return needs_sync


def demonstrate_sync() -> None:
    """
    Demonstrates database synchronization check.
    """
    local_record_ids = [1, 2, 3, 4, 5]
    remote_record_ids = [1, 2, 3, 4, 5]
    local_hash_values = ["abc123", "def456", "ghi789", "jkl012", "mno345"]
    remote_hash_values = ["abc123", "MODIFIED", "ghi789", "jkl012", "MODIFIED"]
    
    out_of_sync = sync_database_records(
        local_record_ids, remote_record_ids,
        local_hash_values, remote_hash_values
    )
    
    print(f"\n{len(out_of_sync)}/{len(local_record_ids)} records need syncing: {out_of_sync}")


if __name__ == "__main__":
    demonstrate_sync()
