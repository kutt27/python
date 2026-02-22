"""
Topic: Debugging Data Pipelines.

Breaking down a pipeline into explicit, traceable steps to 
identify where data transformations might be failing.
"""

def pipeline(data: list):
    print(f"[START] Initial data: {data}")
    
    # Step 1: Filter
    filtered = [x for x in data if x > 0]
    print(f"[STEP 1] Filtered (positives only): {filtered}")
    
    # Step 2: Transform
    transformed = [x * 10 for x in filtered]
    print(f"[STEP 2] Transformed (multiplied by 10): {transformed}")
    
    # Step 3: Aggregate
    result = sum(transformed)
    print(f"[END] Final result: {result}")
    
    return result

if __name__ == "__main__":
    pipeline([1, -2, 3, -4, 5])
