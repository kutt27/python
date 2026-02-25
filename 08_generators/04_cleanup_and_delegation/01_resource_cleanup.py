"""
Topic: Resource Cleanup with `close()`.

The `close()` method terminates a generator. You can use a 
`finally` block to ensure that resources like files or 
connections are cleaned up when the generator is stopped early.
"""

def managed_resource():
    print("Opening Resource...")
    try:
        yield "Data from Resource"
        yield "More Data"
    finally:
        # This code runs when the generator finishes OR is closed early
        print("Cleaning up Resource!")

if __name__ == "__main__":
    print("Scenario 1: Full Iteration")
    gen1 = managed_resource()
    for item in gen1:
        print(f"  Got: {item}")
        
    print("\nScenario 2: Early Close")
    gen2 = managed_resource()
    print(f"  Got: {next(gen2)}")
    print("Closing generator early...")
    gen2.close()
