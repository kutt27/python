"""
Topic: Stateful Calculations with `send()`.

Generators can keep track of state (like a running sum or count) 
and update it based on values sent to them interactively.
"""

def moving_average():
    total = 0.0
    count = 0
    average = None
    
    while True:
        # Yield the current average and wait for the next value
        value = yield average
        
        total += value
        count += 1
        average = total / count

if __name__ == "__main__":
    gen = moving_average()
    next(gen) # Prime
    
    print("Calculating Moving Average:")
    for price in [10.0, 20.0, 30.0]:
        avg = gen.send(price)
        print(f"  Sent {price} -> Average is now {avg:.2f}")
