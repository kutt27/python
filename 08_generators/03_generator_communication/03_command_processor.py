"""
Topic: Interactive Command Processor.

Using `send()` to build a simple interactive service that responds 
to specific commands sent by the caller.
"""

def stateful_counter():
    count = 0
    while True:
        command = yield count
        
        if command == "inc":
            count += 1
        elif command == "dec":
            count -= 1
        elif command == "reset":
            count = 0
        else:
            print(f"  [Error] Unknown command: {command}")

if __name__ == "__main__":
    counter = stateful_counter()
    next(counter) # Prime
    
    print(f"Initial Count: {counter.send(None)}") # Sending None is like next()
    print(f"Sending 'inc' -> {counter.send('inc')}")
    print(f"Sending 'inc' -> {counter.send('inc')}")
    print(f"Sending 'dec' -> {counter.send('dec')}")
    print(f"Sending 'reset' -> {counter.send('reset')}")
