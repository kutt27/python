"""
Topic: Guard Clauses.

Using early returns to handle error cases or edge cases first, 
leaving the main logic at the end. This reduces nested `if` 
statements (the "Arrow Anti-pattern").
"""

def process_withdrawal(amount: float, balance: float):
    # Guard 1: Invalid amount
    if amount <= 0:
        return {"error": "Amount must be positive"}
    
    # Guard 2: Insufficient funds
    if amount > balance:
        return {"error": "Insufficient balance"}
    
    # Main Logic (the "Happy Path")
    new_balance = balance - amount
    return {"success": True, "new_balance": new_balance}

if __name__ == "__main__":
    print(process_withdrawal(-10, 100))
    print(process_withdrawal(200, 100))
    print(process_withdrawal(50, 100))
