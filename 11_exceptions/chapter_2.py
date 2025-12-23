"""
Python Exceptions: Try-Except-Else
===================================

Topic: The 'else' block in exception handling

Real-World Applications:
- Database transactions (commit only if no error)
- API calls (process data only if fetch succeeded)
- File operations
"""

import json
from typing import Dict, Any, Optional


def process_transaction(data_str: str) -> bool:
    """
    Process a transaction string.
    
    The 'else' block is executed ONLY if the 'try' block completes
    without raising an exception. This separates error handling code
    from success code.
    """
    print(f"\nProcessing: {data_str}")
    
    try:
        # 1. Validation/Parsing (Risky operation)
        transaction = json.loads(data_str)
        amount = transaction['amount']
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
    except json.JSONDecodeError:
        print("✗ Error: Invalid JSON format")
        return False
    except KeyError:
        print("✗ Error: Missing 'amount' field")
        return False
    except ValueError as e:
        print(f"✗ Error: {e}")
        return False
    else:
        # 2. Execution (Safe to proceed only if step 1 succeeded)
        # This code runs only if NO exception occurred above.
        print(f"✓ Validated amount: ${amount:.2f}")
        print("  -> Committing transaction to database...")
        return True


def main():
    """Demonstrates try-except-else pattern."""
    print("="*70)
    print("TRY-EXCEPT-ELSE PATTERN".center(70))
    print("="*70)
    
    scenarios = [
        '{"amount": 100}',            # Valid
        '{"amount": -50}',            # ValueError
        '{"value": 100}',             # KeyError
        'Invalid JSON',               # JSONDecodeError
    ]
    
    for i, data in enumerate(scenarios, 1):
        print(f"\n[Scenario {i}]")
        success = process_transaction(data)
        print(f"Transaction Status: {'SUCCESS' if success else 'FAILED'}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• 'else' block runs ONLY if try block raises no exceptions")
    print("• Helps prevent accidental catching of exceptions in success logic")
    print("• Makes code intent clearer: Validation vs Processing")
    print("="*70)


if __name__ == "__main__":
    main()