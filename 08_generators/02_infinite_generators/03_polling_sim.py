"""
Topic: Polling Simulations.

Using generators to encapsulate an infinite polling loop that 
periodically checks a status or fetches updates.
"""

import random

def poll_status():
    while True:
        # Simulate check
        status = random.choice(["OK", "OK", "OK", "ERROR"])
        yield status

if __name__ == "__main__":
    monitor = poll_status()
    
    print("Simulating 5 health checks:")
    for i in range(1, 6):
        print(f"  Check {i}: {next(monitor)}")
