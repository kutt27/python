"""
Topic: Async Locks.

AsyncIO is single-threaded, but if you 'await' in the middle of 
an operation, another coroutine can run and modify shared state. 
This is an 'async race condition'.
"""

import asyncio

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = asyncio.Lock()

    async def unsafe_deposit(self, amount):
        """Vulnerable to context switches."""
        curr = self.balance
        # Any 'await' allows other coroutines to execute
        await asyncio.sleep(0.001) 
        self.balance = curr + amount

    async def safe_deposit(self, amount):
        """Protected by a lock."""
        async with self.lock:
            curr = self.balance
            await asyncio.sleep(0.001)
            self.balance = curr + amount

async def runner(account, method_name):
    # Run 100 concurrent deposits
    func = getattr(account, method_name)
    tasks = [func(1) for _ in range(100)]
    await asyncio.gather(*tasks)

async def main():
    # 1. Test Unsafe
    bad_acc = BankAccount()
    await runner(bad_acc, "unsafe_deposit")
    print(f"Unsafe Balance: {bad_acc.balance} (Expected 100)")

    # 2. Test Safe
    good_acc = BankAccount()
    await runner(good_acc, "safe_deposit")
    print(f"Safe Balance:   {good_acc.balance} (Expected 100)")

if __name__ == "__main__":
    asyncio.run(main())
