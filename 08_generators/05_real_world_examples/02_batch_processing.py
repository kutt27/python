"""
Topic: Data Batching.

Generators can wrap an input stream and "chunk" it into fixed-size 
batches, which is often required for database inserts or API calls.
"""

def get_batches(items, size):
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch

if __name__ == "__main__":
    data = range(1, 11) # 10 items
    
    print("Processing Data in Batches of 3:")
    for chunk in get_batches(data, 3):
        print(f"  Uploading Batch: {chunk}")
