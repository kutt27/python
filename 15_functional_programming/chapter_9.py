"""
Functional Python: Data Pipelines
==================================

Topic: Composing generators for processing streams

Real-World Applications:
- Log processing
- ETL (Extract Transform Load)
- Reading large CSVs
"""

from typing import Iterable, Dict, Iterator

# Simulated Data Stream
RAW_LOGS = [
    "INFO: User1 logged in",
    "ERROR: Database connection failed",
    "WARN: Disk usage high",
    "INFO: User2 logged out",
    "ERROR: Null pointer exception",
    "   ", # Empty line
    "info: User3 clicked button" # formatting issue
]

# --- PIPELINE STAGES (each is a generator) ---

def stage_clean(lines: Iterable[str]) -> Iterator[str]:
    """Stage 1: Clean and filter empty lines."""
    for line in lines:
        stripped = line.strip()
        if stripped:
            yield stripped

def stage_parse(lines: Iterable[str]) -> Iterator[Dict]:
    """Stage 2: Parse string into structured dict."""
    for line in lines:
        parts = line.split(":", 1)
        if len(parts) == 2:
            level, msg = parts
            yield {"level": level.upper(), "msg": msg.strip()}

def stage_filter_error(records: Iterable[Dict]) -> Iterator[Dict]:
    """Stage 3: Keep only errors."""
    for record in records:
        if record["level"] == "ERROR":
            yield record

def stage_format(records: Iterable[Dict]) -> Iterator[str]:
    """Stage 4: Format for output."""
    for record in records:
        yield f"ALERT! {record['msg']}"


def main():
    print("="*70)
    print("GENERATOR PIPELINES".center(70))
    print("="*70)
    
    # Compose the pipeline
    # Data flows from top to bottom (lazy evaluation)
    
    s1 = stage_clean(RAW_LOGS)
    s2 = stage_parse(s1)
    s3 = stage_filter_error(s2)
    pipeline = stage_format(s3)
    
    print("Processing Pipeline...")
    
    # Nothing happens until we iterate
    for alert in pipeline:
        print(alert)
        
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Pipelines allow processing INFINITE streams")
    print("• Each stage is decoupled and testable")
    print("• Extremely memory efficient (one item at a time)")
    print("="*70)


if __name__ == "__main__":
    main()
