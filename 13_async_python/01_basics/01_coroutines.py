"""
Topic: Coroutines Basics.

Coroutines are the building blocks of async Python. Defined with 
'async def' and paused with 'await'.
"""

import asyncio

async def say_hello():
    print("Hello...")
    # 'await' yields control back to the event loop
    await asyncio.sleep(1)
    print("...World!")

async def main():
    # Calling a coroutine function returns a coroutine object
    # It does NOT run the code until it is awaited
    print("Main starting")
    await say_hello()
    print("Main finished")

if __name__ == "__main__":
    asyncio.run(main())
