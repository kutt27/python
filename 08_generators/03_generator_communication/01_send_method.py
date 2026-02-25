"""
Topic: Two-way communication with `send()`.

The `send()` method allows you to pass values BACK into the generator. 
The value you send becomes the result of the `yield` expression 
inside the function.
"""

def talkative_generator():
    print("Generator: I'm waiting for a value...")
    # 'yield' returns a value to the caller, AND receives one back via send()
    received = yield "Ready!"
    print(f"Generator: I received: '{received}'")
    yield f"Thanks for sending '{received}'"

if __name__ == "__main__":
    gen = talkative_generator()
    
    # 1. You MUST "prime" the generator first with next()
    initial_status = next(gen)
    print(f"Caller: Generator says: {initial_status}")
    
    # 2. Use send() to pass a value in. 
    # This resumes the generator and provides the value for the 'yield' expression.
    response = gen.send("Hello Generator!")
    print(f"Caller: Generator says: {response}")
