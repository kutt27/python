"""
Indexed Backup creation.
"""

from typing import List

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


def demonstrate_backup() -> None:
    """
    Demonstrates indexed backup creation.
    """
    files_to_backup = ["config.json", "database.db", "logs.txt"]
    create_indexed_backup(files_to_backup)


if __name__ == "__main__":
    demonstrate_backup()
